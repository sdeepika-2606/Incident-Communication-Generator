
import unittest

from app.incident_parser import load_incident
from app.communication_generator import generate_communication


class TestCommunicationGenerator(unittest.TestCase):

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

    def test_technical_communication(self):
        output = self.generate("technical responders")

        self.assertIn("TECHNICAL INCIDENT UPDATE", output)
        self.assertIn("CONFIRMED FACTS", output)
        self.assertIn("REQUIRES INVESTIGATION", output)

    def test_management_communication(self):
        output = self.generate("service owner")

        self.assertIn("MANAGEMENT INCIDENT UPDATE", output)
        self.assertIn("BUSINESS IMPACT", output)
        self.assertIn("RESPONSE", output)

    def test_staff_communication(self):
        output = self.generate("staff")

        self.assertIn("STAFF SECURITY NOTICE", output)
        self.assertIn("WHAT STAFF SHOULD DO", output)

    def test_all_outputs_include_incident_id(self):
        for audience in [
            "technical responders",
            "service owner",
            "staff"
        ]:
            with self.subTest(audience=audience):
                output = self.generate(audience)
                self.assertIn("RK-INC-TRAIN-204", output)

    def test_all_outputs_include_next_update_and_contact(self):
        for audience in [
            "technical responders",
            "service owner",
            "staff"
        ]:
            with self.subTest(audience=audience):
                output = self.generate(audience)
                self.assertIn(self.next_update, output)
                self.assertIn(self.contact_route, output)

    def test_unconfirmed_facts_are_not_presented_as_confirmed(self):
        output = self.generate("technical responders")

        self.assertIn("REQUIRES INVESTIGATION", output)
        self.assertIn("Whether credentials were stolen.", output)
        self.assertIn("Whether data was accessed or copied.", output)

    def test_unsupported_audience_is_rejected(self):
        with self.assertRaises(ValueError):
            self.generate("unauthorised audience")

    def test_missing_next_update_is_rejected(self):
        with self.assertRaises(ValueError):
            generate_communication(
                self.incident,
                "staff",
                "",
                self.contact_route
            )

    def test_missing_contact_route_is_rejected(self):
        with self.assertRaises(ValueError):
            generate_communication(
                self.incident,
                "staff",
                self.next_update,
                ""
            )


if __name__ == "__main__":
    unittest.main()
