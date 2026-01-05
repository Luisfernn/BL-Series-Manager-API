from fastapi import FastAPI
from app.api.routes.series import router as series_router


app = FastAPI()

app.include_router(series_router)


@app.get("/health")
def health():
    return {"status": "ok"}