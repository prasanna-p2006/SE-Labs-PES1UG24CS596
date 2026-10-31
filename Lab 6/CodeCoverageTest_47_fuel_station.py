
import pytest
from fuel_station import fuel_bill, pump_allowed, session_status


# =====================================
# 1. FUEL BILL TEST CASES
# =====================================

def test_invalid_fuel_grade():
    with pytest.raises(ValueError):
        fuel_bill("petrol", 20, "gold")


def test_negative_litres():
    with pytest.raises(ValueError):
        fuel_bill("regular", -5, "silver")


def test_litres_within_covered_limit():
    assert fuel_bill("regular", 8, "silver") == 0


def test_gold_customer_regular_fuel():
    assert fuel_bill("regular", 20, "gold") == 525


def test_diesel_fuel():
    assert fuel_bill("diesel", 25, "silver") == 450


def test_regular_fuel_exactly_30_extra_litres():
    assert fuel_bill("regular", 40, "silver") == 3150


def test_regular_fuel_above_30_extra_litres():
    assert fuel_bill("regular", 50, "silver") == 3960


def test_gold_customer_above_30_extra_litres():
    assert fuel_bill("regular", 60, "gold") == 4275


# =====================================
# 2. PUMP ALLOWED TEST CASES
# =====================================

def test_fleet_request_allowed():
    assert pump_allowed(150, 3, True) is True


def test_fleet_request_exceeds_limit():
    assert pump_allowed(250, 3, True) is False


def test_non_fleet_request_allowed():
    assert pump_allowed(30, 1, False) is True


def test_non_fleet_request_exceeds_limit():
    assert pump_allowed(70, 1, False) is False


def test_non_fleet_multiple_containers():
    assert pump_allowed(30, 2, False) is False


# =====================================
# 3. SESSION STATUS TEST CASES
# =====================================

def test_card_payment_active():
    assert session_status(60, True, False) == "active"


def test_cash_payment_active():
    assert session_status(30, False, False) == "active"


def test_night_session_active():
    assert session_status(90, True, True) == "active"


def test_session_warning():
    assert session_status(50, True, False) == "warning"


def test_session_timed_out():
    assert session_status(44, True, False) == "timed_out"
