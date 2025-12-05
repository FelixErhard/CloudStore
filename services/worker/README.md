# Worker Service

Minimal worker service for CI testing.

Structure:
- `src/worker.py` - simple entrypoint (no real RabbitMQ in CI)
- `src/event_processor.py` - contains EventProcessor class
- `requirements.txt` - dependencies
- `Dockerfile` - builds the worker image
- `tests/test_event_processor.py` - unit tests
