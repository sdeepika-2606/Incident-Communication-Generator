
# Incident Communication Generator
## System Architecture and Technical Design

### 1. Project Overview

The Incident Communication Generator is a Python-based SOC communication automation tool developed for Task ID 2438.

It transforms structured cybersecurity incident information into three audience-specific communications:

- Technical Responders
- Service Owner
- Staff

The system aims to improve incident communication consistency, accuracy, clarity and reliability.

### 2. System Architecture

The application follows a modular architecture.

```text
              INCIDENT FACTS
             incident_facts.json
                     |
                     v
              INCIDENT PARSER
             incident_parser.py
                     |
                     v
              JSON SCHEMA CHECK
             incident_schema.json
                     |
                     v
             COMMUNICATION GENERATOR
          communication_generator.py
                     |
          +----------+----------+
          |          |          |
          v          v          v
       Technical  Management   Staff
       Responders   Owner     Notification
          |          |          |
          +----------+----------+
                     |
                     v
              OUTPUT VALIDATOR
                validator.py
                     |
                     v
             GENERATED MARKDOWN
                     |
          +----------+----------+
          |          |          |
          v          v          v
       Technical  Management   Staff
        Report      Update    Notification
```

### 3. Module Description

#### 3.1 Incident Parser

File: `app/incident_parser.py`

Responsibilities:
- Reads structured incident information.
- Loads the JSON schema.
- Validates required fields and data types.
- Rejects invalid incident information.
- Provides validated incident data to the generator.

#### 3.2 Communication Generator

File: `app/communication_generator.py`

Responsibilities:
- Accepts validated incident information.
- Generates audience-specific communication.
- Separates confirmed facts from unconfirmed information.
- Includes UTC generation time.
- Includes the operator-provided next update time and contact route.
- Uses audience-appropriate language.

#### 3.3 Output Validator

File: `app/validator.py`

Responsibilities:
- Checks incident identification.
- Checks required update and contact fields.
- Checks for confirmed information sections.
- Checks for clearly identified uncertainty.
- Returns validation status and error messages.

Note: The validator performs structural checks. It does not independently prove the factual accuracy of generated statements.

#### 3.4 Main Application

File: `app/main.py`

Responsibilities:
- Connects the parser, generator and validator.
- Collects required operator inputs.
- Generates all configured audience communications.
- Validates generated messages.
- Saves successful outputs in their respective directories.

### 4. Input Data

The application uses structured JSON incident information containing:

- Incident ID
- Fictional organisation
- Incident status
- Confirmed facts
- Unconfirmed information
- Target audiences
- Communication rules

The operator separately provides:
- Next update time in UTC
- Approved contact route

These values are not automatically invented by the application.

### 5. Output Design

| Audience | Generated file |
|---|---|
| Technical Responders | technical_update.md |
| Service Owner | management_update.md |
| Staff | staff_notification.md |

Each communication includes incident identification, status, confirmed information, uncertainty, relevant impact information, next update and contact details.

### 6. Security and Reliability Considerations

The application follows these communication safeguards:

1. Confirmed facts and hypotheses remain separate.
2. Individuals are not blamed without evidence.
3. Unverified data access is not presented as confirmed.
4. Recovery times are not promised without validation.
5. Required operator inputs are checked.
6. Invalid incident data is rejected.
7. Generated reports undergo structural validation before saving.

### 7. Technology Stack

- Programming Language: Python 3
- Data Format: JSON
- Schema Validation: JSON Schema
- Library: jsonschema
- Output Format: Markdown
- Testing Framework: Python unittest
- Development Environment: Visual Studio Code / PowerShell

### 8. Current Testing Status

The project currently contains four test modules:

| Test module | Test cases |
|---|---:|
| Parser | 5 |
| Generator | 9 |
| Validator | 7 |
| Generated outputs | 7 |
| Total | 28 |

All 28 tests passed in the current test run.

### 9. Limitations

- The application uses structured input rather than live SIEM integrations.
- Generated recommendations require human review and approval.
- Structural validation cannot guarantee semantic accuracy.
- The application does not independently investigate or confirm an incident.
- Contact routes and update times must be supplied by an authorised operator.

### 10. Future Enhancements

Potential future improvements include:

- SIEM integration.
- Role-based access control.
- HTML and PDF report generation.
- Audit logging.
- Advanced semantic validation.
- Approval workflows before communication distribution.

### 11. Conclusion

The Incident Communication Generator provides a modular foundation for producing consistent cybersecurity incident communications for different organisational audiences.

It combines structured incident parsing, audience-specific generation, validation and file output while maintaining a clear distinction between confirmed evidence and unresolved questions.
