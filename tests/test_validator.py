

import unittest

from app.incident_parser import load_incident
from app.communication_generator import generate_communication
from app.validator import validate_output


class TestOutputValidator(unittest.TestCase):

    def setUp(self):
        self.incident = load_incident()
        self.next_update = "2026-11-10 18:00 UTC"
        self.contact_route = "Approved IT Security Helpdesk"

    def generate(self, audience):
        return generate_communication(
            self.incident,
            audience,
            self.next_update,
            self.contact_route
        )

    def test_technical_output_validation(self):
        output = self.generate("technical responders")
        result = validate_output(output, self.incident)
        self.assertTrue(result["valid"], result["errors"])

    def test_management_output_validation(self):
        output = self.generate("service owner")
        result = validate_output(output, self.incident)
        self.assertTrue(result["valid"], result["errors"])

    def test_staff_output_validation(self):
        output = self.generate("staff")
        result = validate_output(output, self.incident)
        self.assertTrue(result["valid"], result["errors"])

    def test_missing_incident_id_is_detected(self):
        output = "CONFIRMED FACTS\nNEXT UPDATE: 18:00\nCONTACT: Helpdesk"
        result = validate_output(output, self.incident)

        self.assertFalse(result["valid"])
        self.assertTrue(
            any(
                self.incident["incident_id"] in error
                for error in result["errors"]
            )
        )

    def test_missing_contact_is_detected(self):
        output = (
            "RK-INC-TRAIN-204\n"
            "CONFIRMED FACTS\n"
            "REQUIRES INVESTIGATION\n"
            "NEXT UPDATE: 18:00"
        )
        result = validate_output(output, self.incident)

        self.assertFalse(result["valid"])
        self.assertTrue(
            any("CONTACT" in error for error in result["errors"])
        )

    def test_missing_uncertainty_section_is_detected(self):
        output = (
            "RK-INC-TRAIN-204\n"
            "CONFIRMED FACTS\n"
            "NEXT UPDATE: 18:00\n"
            "CONTACT: Helpdesk"
        )
        result = validate_output(output, self.incident)

        self.assertFalse(result["valid"])
        self.assertTrue(
            any("Unconfirmed" in error for error in result["errors"])
        )

    def test_empty_output_is_rejected(self):
        result = validate_output("", self.incident)

        self.assertFalse(result["valid"])
        self.assertGreater(len(result["errors"]), 0)


if __name__ == "__main__":
    unittest.main()
