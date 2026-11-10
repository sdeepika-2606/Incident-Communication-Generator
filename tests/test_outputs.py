
import unittest
from pathlib import Path

from app.incident_parser import load_incident


PROJECT_ROOT = Path(__file__).resolve().parent.parent


OUTPUT_FILES = {
    "technical responders": (
        PROJECT_ROOT / "outputs" / "technical_report"
        / "technical_update.md"
    ),
    "service owner": (
        PROJECT_ROOT / "outputs" / "management_updates"
        / "management_update.md"
    ),
    "staff": (
        PROJECT_ROOT / "outputs" / "user_notifications"
        / "staff_notification.md"
    )
}


class TestGeneratedOutputFiles(unittest.TestCase):

    def setUp(self):
        self.incident = load_incident()

    def read_output(self, audience):
        output_file = OUTPUT_FILES[audience]

        self.assertTrue(
            output_file.exists(),
            f"Generated file is missing: {output_file}"
        )

        return output_file.read_text(encoding="utf-8")

    def test_all_three_output_files_exist(self):
        for audience in OUTPUT_FILES:
            with self.subTest(audience=audience):
                self.assertTrue(
                    OUTPUT_FILES[audience].exists()
                )

    def test_all_outputs_contain_incident_id(self):
        for audience in OUTPUT_FILES:
            with self.subTest(audience=audience):
                output = self.read_output(audience)
                self.assertIn(
                    self.incident["incident_id"],
                    output
                )

    def test_all_outputs_preserve_confirmed_facts(self):
        for audience in OUTPUT_FILES:
            with self.subTest(audience=audience):
                output = self.read_output(audience)

                for fact in self.incident["confirmed_facts"]:
                    self.assertIn(fact, output)

    def test_all_outputs_preserve_unconfirmed_facts(self):
        for audience in OUTPUT_FILES:
            with self.subTest(audience=audience):
                output = self.read_output(audience)

                for fact in self.incident["not_yet_confirmed"]:
                    self.assertIn(fact, output)

    def test_all_outputs_include_update_and_contact(self):
        for audience in OUTPUT_FILES:
            with self.subTest(audience=audience):
                output = self.read_output(audience)

                self.assertIn("NEXT UPDATE:", output)
                self.assertIn("CONTACT:", output)

    def test_all_outputs_include_utc_timestamp(self):
        for audience in OUTPUT_FILES:
            with self.subTest(audience=audience):
                output = self.read_output(audience)
                self.assertIn("AS OF (UTC):", output)

    def test_audience_specific_headings(self):
        expected_headings = {
            "technical responders": "TECHNICAL INCIDENT UPDATE",
            "service owner": "MANAGEMENT INCIDENT UPDATE",
            "staff": "STAFF SECURITY NOTICE"
        }

        for audience, heading in expected_headings.items():
            with self.subTest(audience=audience):
                output = self.read_output(audience)
                self.assertIn(heading, output)


if __name__ == "__main__":
    unittest.main()
