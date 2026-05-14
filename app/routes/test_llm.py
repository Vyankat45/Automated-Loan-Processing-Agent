from fastapi import APIRouter
from app.services.llm_service import generate_response

router = APIRouter()


@router.get("/test-llm")
def test_llm():

    prompt = """
    You are a banking AI assistant.

    Explain PAN card validation in simple words.
    """

    response = generate_response(prompt)

    return {
        "response": response
    }