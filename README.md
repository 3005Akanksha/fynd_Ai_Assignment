🧠 AI Review Analysis System

A lightweight AI-powered feedback analysis platform that collects user reviews, generates AI insights, and displays them through separate User and Admin dashboards.
Built using FastAPI, LLM-based prompt engineering, and persistent storage, deployed on Render and Vercel.

🚀 Key Features

User Dashboard
Submit rating (1–5) and review text
Receive AI-generated response

Admin Dashboard
View all reviews
See AI summary and recommended action
Auto-refresh for near real-time updates

AI Capabilities
Review summarization
Recommended next actions
Polite user-facing responses
Strict JSON-based outputs

🧩 Tech Stack
Frontend: HTML, CSS, JavaScript
Backend: FastAPI (Python)
Database: SQLite
AI: Prompt-based LLM generation
Deployment: Render (Backend), Vercel (Frontend)

🧪 Prompt Engineering & Evaluation

Multiple prompt versions tested
Improvements:
JSON-only outputs
Reduced verbosity
Clear separation of response, summary, and action
Evaluated on ~200 review samples
Final prompt produced stable and consistent results

⚖️ Trade-offs & Limitations

SQLite used for simplicity over scalability
CPU-only inference due to free-tier constraints
No authentication implemented
Not designed for high-concurrency production use
