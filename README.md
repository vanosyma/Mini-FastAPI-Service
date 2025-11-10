# Mini-FastAPI-Service
A minimal FastAPI app that recommends hospital departments based on patient symptoms.

# Requirements
- Python 3.9+
- FastAPI
- Uvicorn

# Installation
pip install fastapi uvicorn

# Run
uvicorn main:app --reload

# Test Endpoint
POST http://localhost:8000/recommend
Body:
```{
  "gender": "female",
  "age": 62,
  "symptoms": ["pusing", "mual", "sulit berjalan"]
}

Response:
{
  "recommended_department": "Neurology"
}
