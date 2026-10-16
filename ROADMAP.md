# Roadmap

Small, ordered steps to build `bakery-orders-api` into a polished, interview-ready project.
Tick each box in the same commit that completes the step.

- [x] 1. Project skeleton: `pyproject.toml`, `.gitignore`, `.env.example`, `app/` package, MIT license
- [x] 2. FastAPI app with `/health` endpoint and a first pytest test
- [ ] 3. Configuration via environment variables (pydantic-settings)
- [ ] 4. SQLAlchemy setup, database session dependency, and `Order` / `OrderItem` models
- [ ] 5. Pydantic schemas for creating and reading orders
- [ ] 6. `POST /orders` and `GET /orders/{id}` endpoints
- [ ] 7. `GET /orders` (with status filter) and `PATCH /orders/{id}/status`
- [ ] 8. Alembic migrations for the schema
- [ ] 9. Test suite against SQLite/Postgres with fixtures; cover happy paths and 404/422 errors
- [ ] 10. Ruff lint + format config; make `ruff check` and `ruff format --check` pass
- [ ] 11. Multi-stage, non-root Dockerfile and `.dockerignore`
- [ ] 12. `docker-compose.yml` with API + PostgreSQL + healthchecks for local dev
- [ ] 13. GitHub Actions CI: lint and test jobs
- [ ] 14. CI: Docker build job (with layer caching)
- [ ] 15. Release workflow: publish image to GHCR on `v*` version tags
- [ ] 16. Dependabot for pip, Docker and GitHub Actions
- [ ] 17. Prometheus-style `/metrics` endpoint (request count, latency) for later projects
- [ ] 18. README: overview, Mermaid architecture diagram, run/test instructions, API examples
- [ ] 19. README status badges (CI, release, license) and a "what this demonstrates" section
- [ ] 20. Final polish: tag `v0.1.0`, verify GHCR image pulls and runs
