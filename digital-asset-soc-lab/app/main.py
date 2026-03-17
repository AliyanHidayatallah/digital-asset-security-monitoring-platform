from fastapi import FastAPI

app = FastAPI(title="Digital Asset SOC & Custody Lab")

@app.get("/")
def root():
    return {"message": "Digital Asset SOC Lab is running"}

@app.get("/health")
def health():
    return {"status": "ok"}