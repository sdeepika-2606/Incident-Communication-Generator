# Incident Communications Generator 
An automated Python-based cybersecurity tool that transforms structured incident data into clear, audience-specific communication reports for technical responders, management, and staff. It includes JSON validation, automated Markdown generation, and output verification to support accurate and consistent incident communication.
<div align="center">
<img src="Redkross%20Research%20Foundation.png" alt="RedKross Research Foundation Logo" width="300"/>

cybersecurity incident-response incident-communication soc-operations python automation json-schema threat-detection markdown security-tools
<p>
  <img src="https://img.shields.io/badge/Domain-Cybersecurity-0A7EA4?style=for-the-badge" alt="Cybersecurity"/>
  <img src="https://img.shields.io/badge/Focus-Incident%20Response-6C5CE7?style=for-the-badge" alt="Incident Response"/>
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge" alt="Python"/>
</p>
</div>

**RedKross Research Foundation — Internship Task**

# Incident Communication Generator

**Task ID:** 2438 – Incident Communication Generator  
**Track:** SOC Operation and Threat Detection  
**Organisation:** RedKross Research Foundation  
**Language:** Python 3.12

---

## 1. Project Overview

The Incident Communication Generator is a Python-based application designed to automate cybersecurity incident communication for different organisational audiences.

It converts structured incident facts into three separate communication reports:

1. Technical Responders
2. Service Owner
3. Staff

The application focuses on factual accuracy, clear communication, and separation of confirmed evidence from unverified information.

## 2. Problem Statement

During cybersecurity incidents, different stakeholders require different levels of technical detail.

Manually preparing multiple incident updates can lead to inconsistent information, unsupported assumptions, and unclear communication.

This project addresses the problem by generating structured, audience-specific incident updates from a single validated incident data source.

## 3. Key Features

- Structured JSON incident input.
- JSON Schema validation.
- Three audience-specific communication formats.
- Separation of confirmed and unconfirmed facts.
- UTC generation timestamp.
- Operator-provided next update time.
- Operator-provided approved contact route.
- Output validation.
- Automated Markdown report generation.
- Unit testing using Python unittest.

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application development |
| JSON | Incident data storage |
| JSON Schema | Input validation |
| jsonschema | Schema validation library |
| Markdown | Generated reports |
| unittest | Automated testing |

## 5. Project Structure

```text
Incident_Communication_Generator/
│
├── incident_facts.json
├── status_update_template.md
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── incident_parser.py
│   ├── communication_generator.py
│   ├── templates.py
│   └── validator.py
│
├── data/
│   ├── sample_incidents.json
│   └── incident_schema.json
│
├── tests/
│   ├── test_parser.py
│   ├── test_generator.py
│   ├── test_validator.py
│   └── test_outputs.py
│
├── outputs/
│   ├── technical_report/
│   ├── management_updates/
│   └── user_notifications/
│
├── evidence/
│
├── docs/
│   ├── architecture.md
│   └── test_documentation.md
│
├── requirements.txt
├── README.md
└── .gitignore
```

## 6. Installation

### Prerequisites

- Python 3.12 or compatible Python 3 version.
- PowerShell or another terminal.
- pip package manager.

### Step 1: Create a virtual environment

```powershell
python -m venv .venv
```

### Step 2: Activate the environment

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\.venv\Scripts\Activate.ps1
```

### Step 3: Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## 7. Application Execution

Run the application from the project root:

```powershell
python -m app.main
```

The operator is prompted to provide:

- Next update time in UTC.
- Approved contact route.

The application then loads the incident facts, generates communications, validates the outputs, and saves the reports.

## 8. Generated Reports

| Audience | Output file |
|---|---|
| Technical Responders | `outputs/technical_report/technical_update.md` |
| Service Owner | `outputs/management_updates/management_update.md` |
| Staff | `outputs/user_notifications/staff_notification.md` |

## 9. Testing

Execute the complete test suite:

```powershell
python -m unittest discover -s tests -v
```

### Test Results

| Module | Passed | Failed |
|---|---:|---:|
| Parser | 5 | 0 |
| Generator | 9 | 0 |
| Validator | 7 | 0 |
| Output Tests | 7 | 0 |
| **Total** | **28** | **0** |

All 28 test cases passed in the recorded final test run.

## 10. Evidence Documentation

The `evidence/` directory contains screenshots demonstrating:

- Parser test results.
- Generator test results.
- Validator test results.
- Generated output file test results.
- Technical responder report.
- Service owner report.
- Staff security notification.
- Final combined test results.

## 11. Security and Reliability

The application follows these safeguards:

- Confirmed facts are kept separate from unconfirmed information.
- No individual is identified as responsible without evidence.
- Unverified data access is not presented as confirmed.
- Recovery times are not promised without validation.
- Required operator inputs are checked.
- Invalid incident data is rejected.
- Generated reports are structurally validated.

## 12. Limitations

- The application uses predefined structured incident data.
- It does not connect directly to SIEM platforms.
- It does not independently investigate security incidents.
- Structural validation does not guarantee semantic accuracy.
- Generated recommendations require authorised human review.
- Contact routes and next update times must be provided by the operator.

## 13. Future Enhancements

- SIEM integration.
- Role-based access control.
- PDF and HTML report generation.
- Audit logging.
- Advanced semantic validation.
- Communication approval workflows.
- Secure report distribution.

## 14. Conclusion

The Incident Communication Generator demonstrates how structured incident data can be transformed into consistent and audience-specific cybersecurity communications.

The project combines input validation, modular Python development, automated communication generation, output validation, and unit testing.

The final recorded test suite completed successfully with 28 passed tests and zero failures.

