from fastapi import APIRouter

from app.agents.ocr_agent import extract_text
from app.agents.validation_agent import validate_pan
from app.agents.risk_agent import analyze_risk

router = APIRouter()


@router.get("/full-analysis")
def full_analysis(image_path: str):

    text = extract_text(image_path)

    validation = validate_pan(text)

    risk = analyze_risk(validation["valid"])

    return {
        "ocr_text": text,
        "validation": validation,
        "risk_analysis": risk
    }