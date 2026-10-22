# bakery-orders-api

FastAPI + PostgreSQL order API for a small cottage bakery (Dang Good Pies).

> Work in progress: see [ROADMAP.md](ROADMAP.md) for the build plan.

## Database migrations

Schema changes are managed with Alembic. The database URL comes from `DATABASE_URL`.

```bash
alembic upgrade head                                  # apply all migrations
alembic revision --autogenerate -m "describe change"  # after editing app/models.py
```
