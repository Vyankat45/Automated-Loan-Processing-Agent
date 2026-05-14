from langchain_ollama import OllamaLLM


llm = OllamaLLM(
    model="phi3",
    base_url="https://reenact-structure-frosting.ngrok-free.dev"
)


def generate_response(prompt: str):

    response = llm.invoke(prompt)

    return response