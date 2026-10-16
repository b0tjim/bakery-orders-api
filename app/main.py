from fastapi import FastAPI

app = FastAPI(title="Bakery Orders API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness probe used by Docker, Compose and Kubernetes."""
    return {"status": "ok"}
