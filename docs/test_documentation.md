
# Incident Communication Generator
## Software Testing and Validation Documentation

### 1. Introduction

This document describes the testing methodology used to verify the Incident Communication Generator.

The application was tested using Python's built-in unittest framework to verify individual modules and the generated communication files.

### 2. Testing Objectives

The testing process aims to verify:

- Correct loading of incident information.
- JSON schema validation.
- Audience-specific communication generation.
- Preservation of confirmed and unconfirmed facts.
- Detection of missing required fields.
- Correct generation and storage of output files.
- Consistency across all three audience outputs.

### 3. Testing Environment

| Component | Configuration |
|---|---|
| Operating System | Windows 11 |
| Programming Language | Python 3.12 |
| Testing Framework | unittest |
| Data Format | JSON |
| Output Format | Markdown |
| Validation Library | jsonschema |

### 4. Test Modules

#### 4.1 Parser Tests

File: `tests/test_parser.py`

Tests:
- Successful incident loading.
- Confirmed fact loading.
- Preservation of unconfirmed facts.
- Rejection of missing incident ID.
- Rejection of invalid incident status.

Result: 5/5 passed.

Evidence: `evidence/Parser_Test_Results.png`

#### 4.2 Generator Tests

File: `tests/test_generator.py`

Tests:
- Technical communication generation.
- Management communication generation.
- Staff communication generation.
- Incident ID inclusion.
- Next update and contact inclusion.
- Rejection of missing next update.
- Rejection of missing contact route.
- Rejection of unsupported audience.
- Separation of unconfirmed information.

Result: 9/9 passed.

Evidence: `evidence/Generator_Test_Results.png`

#### 4.3 Validator Tests

File: `tests/test_validator.py`

Tests:
- Technical output validation.
- Management output validation.
- Staff output validation.
- Detection of missing incident ID.
- Detection of missing contact information.
- Detection of missing uncertainty section.
- Rejection of empty output.

Result: 7/7 passed.

Evidence: `evidence/Validator_Test_Results.png`

#### 4.4 Generated Output Tests

File: `tests/test_outputs.py`

Tests:
- Existence of all three generated files.
- Incident ID preservation.
- Confirmed fact preservation.
- Unconfirmed fact preservation.
- Next update and contact inclusion.
- UTC timestamp inclusion.
- Audience-specific headings.

Result: 7/7 passed.

Evidence: `evidence/Output_File_Test_Results.png`

### 5. Overall Test Results

| Module | Passed | Failed |
|---|---:|---:|
| Parser | 5 | 0 |
| Generator | 9 | 0 |
| Validator | 7 | 0 |
| Output Tests | 7 | 0 |
| Total | 28 | 0 |

Overall result: 28 tests passed, 0 failed.

### 6. Execution Command

The complete test suite can be executed using:

```powershell
python -m unittest discover -s tests -v
```

### 7. Functional Execution Test

The application was executed using:

```powershell
python -m app.main
```

The operator supplied a sample next update time and approved contact route.

The application successfully generated:

1. Technical responder report.
2. Service owner update.
3. Staff security notification.

Evidence:
- `evidence/Technical_Update_Output.png`
- `evidence/Management_Update_Output.png`
- `evidence/Staff_Notification_Output.png`

### 8. Testing Conclusion

The current test suite confirms that the parser, generator, validator and saved output files satisfy the implemented test cases.

All 28 tests passed during the recorded test run.

These results demonstrate functional and structural correctness for the supplied test scenario. They do not replace manual review of incident facts or prove the accuracy of real-world incident conclusions.
