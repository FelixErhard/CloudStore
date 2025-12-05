import sys
import os
import pytest

# Ensure the service src dir is on sys.path when tests run from the service folder
HERE = os.path.dirname(__file__)
SRC_DIR = os.path.abspath(os.path.join(HERE, '..', 'src'))
sys.path.insert(0, SRC_DIR)

from event_processor import EventProcessor


def test_event_processor_success():
    processor = EventProcessor()
    event = {"resource_type": "test_resource", "parameters": {"name": "x"}}
    result = processor.process(event)
    assert result["status"] == "ok"
    assert "resource" in result


def test_event_processor_invalid():
    processor = EventProcessor()
    with pytest.raises(ValueError):
        processor.process({})
