
def validate_output(output, incident):
    """Validate required communication fields and uncertainty indicators."""

    errors = []

    required_fields = [
        incident["incident_id"],
        "NEXT UPDATE:",
        "CONTACT:"
    ]

    for field in required_fields:
        if field.lower() not in output.lower():
            errors.append(f"Missing required information: {field}")

    confirmation_headings = [
        "CONFIRMED FACTS",
        "CONFIRMED INFORMATION",
        "WHAT WE KNOW",
        "CURRENT SITUATION"
    ]

    if not any(
        heading.lower() in output.lower()
        for heading in confirmation_headings
    ):
        errors.append("Confirmed information section is missing.")

    uncertainty_markers = [
        "under investigation",
        "requires investigation",
        "not yet confirmed",
        "unconfirmed information"
    ]

    if not any(
        marker in output.lower()
        for marker in uncertainty_markers
    ):
        errors.append("Unconfirmed information is not clearly identified.")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }
