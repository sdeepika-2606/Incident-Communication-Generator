
import json
from pathlib import Path

from jsonschema import Draft202012Validator


PROJECT_ROOT = Path(__file__).resolve().parent.parent

INCIDENT_FILE = PROJECT_ROOT / "data" / "sample_incidents.json"
SCHEMA_FILE = PROJECT_ROOT / "data" / "incident_schema.json"


class IncidentParserError(Exception):
    """Raised when incident data cannot be loaded or validated."""


def load_json(file_path):
    """Load JSON data from a file safely."""
    try:
        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        raise IncidentParserError(
            f"Required file not found: {file_path}"
        )

    except json.JSONDecodeError as error:
        raise IncidentParserError(
            f"Invalid JSON in {file_path.name}: {error}"
        )


def validate_incident(incident, schema):
    """Validate incident information against the JSON schema."""
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(incident), key=lambda e: list(map(str, e.path)))

    if errors:
        error_messages = [
            f"{'.'.join(map(str, error.path)) or 'root'}: {error.message}"
            for error in errors
        ]

        raise IncidentParserError(
            "Incident validation failed:\n" + "\n".join(error_messages)
        )

    return True


def load_incident():
    """Load and validate the project incident facts."""
    incident = load_json(INCIDENT_FILE)
    schema = load_json(SCHEMA_FILE)

    validate_incident(incident, schema)

    return incident
