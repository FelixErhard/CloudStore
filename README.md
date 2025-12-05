# CloudStore - CI Test Setup

This repository contains a minimal CI test setup used to demonstrate the GitHub Actions pipeline.

How to run locally:

1. Build and start test services with docker-compose:

```bash
docker compose -f docker-compose.test.yml up --build
```

2. Run integration tests:

```bash
pytest tests/integration/
```

Services:
- `services/api` - minimal Flask app with `/health` endpoint
- `services/worker` - minimal worker module with EventProcessor (unit-tested)
