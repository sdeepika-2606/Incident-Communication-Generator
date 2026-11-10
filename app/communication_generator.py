
from datetime import datetime, timezone


def generate_communication(incident, audience, next_update, contact_route):
    """Generate a factual incident update for a specific audience."""

    allowed_audiences = {
        "technical responders",
        "service owner",
        "staff"
    }

    if audience not in allowed_audiences:
        raise ValueError(f"Unsupported audience: {audience}")

    if not next_update or not next_update.strip():
        raise ValueError("Next update time is required.")

    if not contact_route or not contact_route.strip():
        raise ValueError("Approved contact route is required.")

    confirmed = "\n".join(
        f"- {fact}" for fact in incident["confirmed_facts"]
    )

    unconfirmed = "\n".join(
        f"- {fact}" for fact in incident["not_yet_confirmed"]
    )

    update = {
        "incident_id": incident["incident_id"],
        "status": incident["status"],
        "as_of_utc": datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M UTC"
        ),
        "confirmed": confirmed,
        "under_investigation": unconfirmed,
        "next_update": next_update,
        "contact_route": contact_route
    }

    if audience == "technical responders":
        return technical_update(incident, update)

    if audience == "service owner":
        return management_update(incident, update)

    return staff_update(incident, update)


def technical_update(incident, update):
    return f"""
TECHNICAL INCIDENT UPDATE
Organisation: {incident['fictional_organisation']}
Incident ID: {update['incident_id']}
Status: {update['status']}
AS OF (UTC): {update['as_of_utc']}

CONFIRMED FACTS:
{update['confirmed']}

REQUIRES INVESTIGATION:
{update['under_investigation']}

RECOMMENDED RESPONSE ACTIONS:
- Review authentication logs and MFA events.
- Validate the privilege event against approved change records.
- Preserve relevant logs for investigation.

IMPACT CURRENTLY KNOWN:
The extent of account compromise and possible data access is not yet confirmed.

NEXT UPDATE: {update['next_update']}
CONTACT: {update['contact_route']}
""".strip()


def management_update(incident, update):
    return f"""
MANAGEMENT INCIDENT UPDATE
Organisation: {incident['fictional_organisation']}
Incident ID: {update['incident_id']}
Status: {update['status']}
AS OF (UTC): {update['as_of_utc']}

CURRENT SITUATION:
An account has experienced repeated failed sign-in events and two unexpected MFA prompts were denied by the user. A privilege event with an unclear change-ticket reference is also being investigated.

CONFIRMED INFORMATION:
{update['confirmed']}

UNCONFIRMED INFORMATION:
{update['under_investigation']}

BUSINESS IMPACT CURRENTLY KNOWN:
The extent of operational impact and possible data exposure has not yet been established.

RECOMMENDED RESPONSE ACTIONS:
- Review authentication activity and MFA events.
- Validate the privilege event against approved change records.
- Assess potential business impact as evidence becomes available.

NEXT UPDATE: {update['next_update']}
CONTACT: {update['contact_route']}
""".strip()


def staff_update(incident, update):
    return f"""
STAFF SECURITY NOTICE
Organisation: {incident['fictional_organisation']}
Incident ID: {update['incident_id']}
Status: {update['status']}
AS OF (UTC): {update['as_of_utc']}

WHAT WE KNOW:
{update['confirmed']}

WHAT IS NOT YET CONFIRMED:
{update['under_investigation']}

IMPACT CURRENTLY KNOWN:
The extent of account compromise and possible data access is not yet confirmed.

WHAT STAFF SHOULD DO:
- Do not approve unexpected MFA requests.
- Report suspicious sign-in notifications through the approved contact route.
- Follow instructions from the authorised IT or security team.

NEXT UPDATE: {update['next_update']}
CONTACT: {update['contact_route']}
""".strip()
