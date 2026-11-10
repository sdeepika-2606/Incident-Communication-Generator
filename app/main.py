
from pathlib import Path

from app.incident_parser import load_incident, IncidentParserError
from app.communication_generator import generate_communication
from app.validator import validate_output


PROJECT_ROOT = Path(__file__).resolve().parent.parent

OUTPUT_DIRECTORIES = {
    "technical responders": PROJECT_ROOT / "outputs" / "technical_report",
    "service owner": PROJECT_ROOT / "outputs" / "management_updates",
    "staff": PROJECT_ROOT / "outputs" / "user_notifications"
}

OUTPUT_FILENAMES = {
    "technical responders": "technical_update.md",
    "service owner": "management_update.md",
    "staff": "staff_notification.md"
}


def main():
    print("=" * 55)
    print(" INCIDENT COMMUNICATION GENERATOR")
    print("=" * 55)

    try:
        incident = load_incident()

        print(f"\nIncident ID : {incident['incident_id']}")
        print(f"Organisation: {incident['fictional_organisation']}")
        print(f"Status      : {incident['status']}")

        print("\nOperator input required")
        next_update = input("Enter next update time (UTC): ").strip()
        contact_route = input("Enter approved contact route: ").strip()

        if not next_update or not contact_route:
            print("\nERROR: Both inputs are required.")
            return

        audiences = incident["audiences"]

        for audience in audiences:
            output = generate_communication(
                incident,
                audience,
                next_update,
                contact_route
            )

            validation = validate_output(output, incident)

            if not validation["valid"]:
                print(f"\nValidation failed for {audience}:")
                for error in validation["errors"]:
                    print(f"- {error}")
                continue

            output_directory = OUTPUT_DIRECTORIES[audience]
            output_directory.mkdir(parents=True, exist_ok=True)

            output_file = (
                output_directory / OUTPUT_FILENAMES[audience]
            )

            output_file.write_text(output + "\n", encoding="utf-8")

            print(f"\n[{audience.upper()}] Generated successfully")
            print(f"Saved to: {output_file.relative_to(PROJECT_ROOT)}")

        print("\n" + "=" * 55)
        print(" COMMUNICATION GENERATION COMPLETED")
        print("=" * 55)

    except (IncidentParserError, ValueError, KeyError) as error:
        print(f"\nERROR: {error}")


if __name__ == "__main__":
    main()
