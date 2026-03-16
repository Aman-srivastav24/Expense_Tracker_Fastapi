from fastapi import FastAPI
app = FastAPI(title="Expense Tracker API", description="API for tracking expenses", version="1.0.0")
@app.get("/")
def health_check():
    return{"status": "API is up and running!"}