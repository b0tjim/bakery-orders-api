from fastapi import FastAPI

from app.metrics import metrics_middleware
from app.metrics import router as metrics_router
from app.routers_orders import router as orders_router

app = FastAPI(title="Bakery Orders API", version="0.1.0")
app.include_router(orders_router)
app.include_router(metrics_router)
app.middleware("http")(metrics_middleware)


@app.get("/health")
def health() -> dict[str, str]:
    """Liveness probe used by Docker, Compose and Kubernetes."""
    return {"status": "ok"}
