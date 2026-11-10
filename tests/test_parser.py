
import unittest

from app.incident_parser import (
    load_incident,
    load_json,
    validate_incident,
    IncidentParserError,
    SCHEMA_FILE
)


class TestIncidentParser(unittest.TestCase):

    def setUp(self):
        self.schema = load_json(SCHEMA_FILE)

    def test_load_incident_successfully(self):
        incident = load_incident()

        self.assertEqual(
            incident["incident_id"],
            "RK-INC-TRAIN-204"
        )

    def test_confirmed_facts_are_loaded(self):
        incident = load_incident()

        self.assertEqual(len(incident["confirmed_facts"]), 3)

    def test_unconfirmed_facts_are_preserved(self):
        incident = load_incident()

        self.assertEqual(len(incident["not_yet_confirmed"]), 3)

    def test_missing_incident_id_is_rejected(self):
        invalid_incident = {
            "fictional_organisation": "Northstar Community Services",
            "status": "investigating",
            "confirmed_facts": ["Test fact"],
            "not_yet_confirmed": [],
            "audiences": ["staff"],
            "communication_rules": ["Keep it factual"]
        }

        with self.assertRaises(IncidentParserError):
            validate_incident(invalid_incident, self.schema)

    def test_invalid_status_is_rejected(self):
        incident = {
            "incident_id": "TEST-001",
            "fictional_organisation": "Test Organisation",
            "status": "unknown",
            "confirmed_facts": ["Test fact"],
            "not_yet_confirmed": [],
            "audiences": ["staff"],
            "communication_rules": ["Keep it factual"]
        }

        with self.assertRaises(IncidentParserError):
            validate_incident(incident, self.schema)


if __name__ == "__main__":
    unittest.main()
