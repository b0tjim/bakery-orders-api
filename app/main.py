from fastapi import FastAPI

from app.routers_orders import router as orders_router

app = FastAPI(title="Bakery Orders API", version="0.1.0")
app.include_router(orders_router)


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness probe used by Docker, Compose and Kubernetes."""
    return {"status": "ok"}
