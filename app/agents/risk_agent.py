from langchain_ollama import OllamaLLM


llm = OllamaLLM(
    model="mistral",
    base_url="https://reenact-structure-frosting.ngrok-free.dev"
)


def analyze_risk(pan_status: bool):

    prompt = f"""
    You are a loan risk analyst.

    PAN Validation Status: {pan_status}

    Analyze the loan risk.

    Return:
    1. Risk Level
    2. Reason
    3. Recommendation
    """

    response = llm.invoke(prompt)

    return response