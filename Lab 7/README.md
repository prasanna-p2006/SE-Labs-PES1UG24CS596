
# Lab 7: Fuzz Testing for Input Validation Bugs

## Objective

To explore fuzz testing using the Hypothesis library and identify input validation bugs in a Python application. The identified bugs were fixed using defensive programming techniques.

## Tools and Technologies

- Python 3.8+
- Hypothesis
- Pytest
- Visual Studio Code

## Project Description

The Fuel Station application contains three functions:

1. `parse_purchase()` - Parses fuel grade and purchase quantity.
2. `volume_average()` - Calculates the average of pump volumes.
3. `payable_bill()` - Calculates the payable bill after applying tax and discount.

## Files

| File | Description |
|---|---|
| `fuel_station.py` | Application containing the three functions |
| `test_fuel_station.py` | Hypothesis fuzz tests and valid-input property tests |
| `Screenshot/` | Screenshots showing the application and test results |

## Installation

Install the required libraries:

```bash
python -m pip install hypothesis pytest
```

## Running the Application

```bash
python fuel_station.py
```

## Running the Tests

```bash
python -m pytest test_fuel_station.py -v
```

## Bugs Identified

Hypothesis generated unexpected inputs and identified the following problems:

- `parse_purchase()` failed with None, empty strings, and missing or empty values.
- `volume_average()` failed with None and empty strings.
- `payable_bill()` failed with None, empty strings, and missing or empty values.

## Bug Fixes

Defensive programming techniques were implemented:

- Input type validation.
- Separator and input format validation.
- Exception handling for invalid numeric conversions.
- Validation of non-finite numeric values.
- Safe fallback return values for invalid inputs.

## Test Results

The application was tested using six tests:

- Three fuzz tests to check whether the functions crash on unexpected inputs.
- Three property-based tests to verify correct behaviour for valid inputs.

**Final Result: 6 passed**

## Screenshots

The `Screenshot` folder contains:

1. `before_application.png` - Original application execution.
2. `failing_tests.png` - Fuzz tests identifying bugs.
3. `after_application.png` - Corrected application execution.
4. `passing_tests.png` - All tests passing after bug fixes.

## Conclusion

Fuzz testing with Hypothesis successfully identified input validation bugs in the Fuel Station application. After implementing defensive programming techniques, all six tests passed, demonstrating improved robustness and correct behaviour for the tested inputs.
