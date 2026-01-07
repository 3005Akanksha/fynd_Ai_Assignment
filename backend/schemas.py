from pydantic import BaseModel

class ReviewRequest(BaseModel):
    rating: int
    review: str

class ReviewResponse(BaseModel):
    ai_response: str
