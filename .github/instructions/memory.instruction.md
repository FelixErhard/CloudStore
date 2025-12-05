---
applyTo: '**'
---

# General Copilot Instruction for CloudStore

This project follows these coding and documentation standards:

1. **Comments and Docstrings:**
   - All code comments, inline explanations, and docstrings must be written in English.
   - This applies to all programming languages and all code files in the repository.
   - Example:
     ```python
     # This function processes incoming events and provisions resources.
     def process_event(event: dict) -> None:
         """Validates the event and runs Terraform provisioning."""
         ...
     ```

2. **Code Quality:**
   - Follow Clean Code principles: clear function separation, meaningful naming, error handling, resource management, and modularity.
   - Use Python best practices for all Python code (PEP8, type hints, context managers, logging, configuration via environment variables).

3. **Security:**
   - Never hardcode credentials or secrets in code files. Use environment variables or secret management systems.

4. **Documentation:**
   - All documentation, including README files and code comments, must be in English.

5. **Extensibility and Structure:**
   - Code should be written to be maintainable and extensible for future features and team collaboration.
   - Where appropriate, use classes to encapsulate related functionality and promote object-oriented design.
   - Split code into multiple files/modules when it improves clarity, maintainability, or reusability.

6. **Testing:**
   - All new features and changes should be covered by appropriate tests.

Please ensure all future code contributions and documentation strictly follow these rules.
