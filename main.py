from fastapi import FastAPI
from pydantic import BaseModel

class PatientInfo(BaseModel):
    gender: str
    age: int
    symptoms: list[str]

def recommendation(patient: PatientInfo) -> str:
    s = [sym.lower() for sym in patient.symptoms]

    if any(x in s for x in ["pusing", "sulit berjalan", "kehilangan keseimbangan"]):
        return "Neurology"
    elif any(x in s for x in ["sesak napas", "batuk", "demam"]):
        return "Pulmonology"
    elif any(x in s for x in ["mual", "sakit perut", "gusi berdarah"]):
        return "Gastroenterology"
    elif any(x in s for x in ["susah tidur"]):
        return "Psychiatry"
    else:
        return "General Medicine"


# FastAPI App
app = FastAPI(
    title="Department Recommendation API",
    version="1.0.0",
)

@app.post("/recommend")
def recommend_department(patient: PatientInfo):
    """
    Endpoint utama untuk memberikan rekomendasi departemen berdasarkan input pasien.
    """
    department = recommendation(patient)
    return {"recommended_department": department}
