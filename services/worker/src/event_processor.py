"""Event processor for Worker service.

This module follows the project's Copilot Instruction: English docstrings and comments,
clean code, and modular structure.
adfizlasd.fukjas
"""

import json
import tempfile
import shutil
import subprocess
import logging
from contextlib import contextmanager
from typing import Dict, Any


class EventProcessor:
    """Processes events and provisions infrastructure using Terraform.

    This is a minimal implementation intended for CI tests. It does not actually
    contact cloud providers. Instead it writes a Terraform config and simulates
    execution by returning a mocked output.
    """

    def process(self, event: Dict[str, Any]) -> Dict[str, Any]:
        """Validate the event and run the provisioning workflow.

        Returns a dictionary with the (mocked) result.
        """
        resource_type = event.get("resource_type")
        parameters = event.get("parameters")
        if not resource_type or not isinstance(parameters, dict):
            logging.error("Invalid event: missing resource_type or parameters")
            raise ValueError("invalid event")

        with self._temporary_directory() as d:
            self._write_terraform_config(d, resource_type, parameters)
            # In CI we don't run real terraform; simulate output
            result = {"status": "ok", "resource": f"{resource_type}.example"}
            logging.info("Simulated provisioning result: %s", result)
            return result

    @staticmethod
    @contextmanager
    def _temporary_directory():
        """Create and clean up a temporary directory."""
        dirpath = tempfile.mkdtemp()
        try:
            yield dirpath
        finally:
            shutil.rmtree(dirpath)

    @staticmethod
    def _write_terraform_config(directory: str, resource_type: str, parameters: Dict[str, Any]) -> None:
        """Write a minimal Terraform configuration file to the given directory."""
        lines = [f'resource "{resource_type}" "example" {{\n']
        for k, v in parameters.items():
            safe_v = str(v).replace('"', '\\"')
            lines.append(f'  {k} = "{safe_v}"\n')
        lines.append('}\n')
        with open(f"{directory}/main.tf", "w", encoding="utf-8") as fh:
            fh.writelines(lines)
