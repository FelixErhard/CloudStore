"""Simple worker entrypoint for CI testing.

In CI we avoid external dependencies (RabbitMQ) and expose a simple function
that can be invoked by tests.
"""

import logging
from .event_processor import EventProcessor


logging.getLogger().setLevel(logging.INFO)


class Worker:
    """Encapsulates worker logic for invocation by tests or runtime.

    The Worker class provides a `handle_event` method that accepts a dict and
    delegates to the EventProcessor.
    """

    def __init__(self) -> None:
        self.processor = EventProcessor()

    def handle_event(self, event: dict) -> dict:
        """Process the provided event and return the result.

        Raises ValueError if the event is invalid.
        """
        return self.processor.process(event)


if __name__ == "__main__":
    # Example run for local manual testing
    w = Worker()
    example = {"resource_type": "aws_instance", "parameters": {"name": "ci-test"}}
    print(w.handle_event(example))
