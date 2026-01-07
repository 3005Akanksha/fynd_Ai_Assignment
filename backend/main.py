from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import re

from database import engine, SessionLocal
from models import Review, Base
from llm import generate_ai_content

# -------------------------------------------------
# App setup
# -------------------------------------------------
app = FastAPI()

# CORS (required for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # for local + deployment
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create DB tables
Base.metadata.create_all(bind=engine)

# -------------------------------------------------
# Schemas
# -------------------------------------------------
class ReviewRequest(BaseModel):
    rating: int
    review: str

class ReviewResponse(BaseModel):
    message: str
    ai_response: str

# -------------------------------------------------
# Routes
# -------------------------------------------------

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.post("/submit-review", response_model=ReviewResponse)
def submit_review(data: ReviewRequest):

    # Validation
    if not data.review.strip():
        raise HTTPException(status_code=400, detail="Review cannot be empty")

    if data.rating < 1 or data.rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be 1 to 5")

    # Call LLM (server-side only ✔️)
    raw_output = generate_ai_content(data.review)

    # Extract JSON from LLM output
    match = re.search(r"\{.*?\}", raw_output, re.DOTALL)
    if not match:
        raise HTTPException(status_code=500, detail="Invalid LLM output")

    ai_json = json.loads(match.group())

    # Save to DB
    db = SessionLocal()
    new_review = Review(
        rating=data.rating,
        review=data.review,
        ai_response=ai_json.get("response", ""),
        ai_summary=ai_json.get("summary", ""),
        ai_action=ai_json.get("action", "")
    )

    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    db.close()

    return {
        "message": "Review submitted successfully",
        "ai_response": new_review.ai_response
    }

@app.get("/reviews")
def get_reviews():
    db = SessionLocal()
    reviews = db.query(Review).all()
    db.close()

    return reviews


