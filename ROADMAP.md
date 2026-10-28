# Roadmap

Small, ordered steps to build `bakery-orders-api` into a polished, interview-ready project.
Tick each box in the same commit that completes the step.

- [x] 1. Project skeleton: `pyproject.toml`, `.gitignore`, `.env.example`, `app/` package, MIT license
- [x] 2. FastAPI app with `/health` endpoint and a first pytest test
- [x] 3. Configuration via environment variables (pydantic-settings)
- [x] 4. SQLAlchemy setup, database session dependency, and `Order` / `OrderItem` models
- [x] 5. Pydantic schemas for creating and reading orders
- [x] 6. `POST /orders` and `GET /orders/{id}` endpoints
- [x] 7. `GET /orders` (with status filter) and `PATCH /orders/{id}/status`
- [x] 8. Alembic migrations for the schema
- [x] 9. Test suite against SQLite/Postgres with fixtures; cover happy paths and 404/422 errors
- [x] 10. Ruff lint + format config; make `ruff check` and `ruff format --check` pass
- [x] 11. Multi-stage, non-root Dockerfile and `.dockerignore`
- [x] 12. `docker-compose.yml` with API + PostgreSQL + healthchecks for local dev
- [x] 13. GitHub Actions CI: lint and test jobs
- [x] 14. CI: Docker build job (with layer caching)
- [x] 15. Release workflow: publish image to GHCR on `v*` version tags
- [x] 16. Dependabot for pip, Docker and GitHub Actions
- [x] 17. Prometheus-style `/metrics` endpoint (request count, latency) for later projects
- [x] 18. README: overview, Mermaid architecture diagram, run/test instructions, API examples
- [x] 19. README status badges (CI, release, license) and a "what this demonstrates" section
- [ ] 20. Final polish: tag `v0.1.0`, verify GHCR image pulls and runs
