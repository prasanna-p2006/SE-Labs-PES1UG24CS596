import pytest
from fuel_station import fuel_bill, pump_allowed, session_status

# Example test cases:
def test_within_covered_litres():
    assert fuel_bill("regular", 8, "silver") == 0

def test_pump_allowed():
    assert pump_allowed(30, 1, False) is True

# Write the rest of the test cases so that the code is 90-100% covered.
