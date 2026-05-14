from fastapi import FastAPI

from app.routes.upload import router as upload_router
from app.routes.analyze import router as analyze_router
from app.routes.test_llm import router as test_router

app = FastAPI(title="AI Loan Processing Agent")

app.include_router(upload_router)
app.include_router(analyze_router)
app.include_router(test_router)


@app.get("/")
def root():
    return {"message": "Backend Running Successfully"}