
import pytest
from fuel_station import fuel_bill, pump_allowed, session_status


# =====================================
# 1. FUEL BILL - VALIDATION BRANCHES
# =====================================

def test_invalid_fuel_grade():
    with pytest.raises(ValueError):
        fuel_bill("petrol", 20, "gold")


def test_valid_fuel_grade():
    assert fuel_bill("regular", 8, "silver") == 0


def test_negative_litres():
    with pytest.raises(ValueError):
        fuel_bill("regular", -5, "silver")


def test_positive_litres():
    assert fuel_bill("regular", 20, "silver") == 1050


# =====================================
# 2. LOYALTY AND FUEL GRADE BRANCHES
# =====================================

def test_gold_regular_customer():
    assert fuel_bill("regular", 20, "gold") == 525


def test_silver_regular_customer():
    assert fuel_bill("regular", 20, "silver") == 1050


def test_gold_diesel_customer():
    assert fuel_bill("diesel", 25, "gold") == 450


def test_silver_diesel_customer():
    assert fuel_bill("diesel", 25, "silver") == 450


def test_premium_fuel():
    assert fuel_bill("premium", 20, "silver") == 525


# =====================================
# 3. EXTRA LITRES AND DISCOUNT BRANCHES
# =====================================

def test_no_extra_litres():
    assert fuel_bill("regular", 10, "silver") == 0


def test_extra_litres_less_than_30():
    assert fuel_bill("regular", 30, "silver") == 2100


def test_extra_litres_exactly_30():
    assert fuel_bill("regular", 40, "silver") == 3150


def test_extra_litres_above_30_silver():
    assert fuel_bill("regular", 50, "silver") == 3960


def test_extra_litres_above_30_gold():
    assert fuel_bill("regular", 60, "gold") == 4275


def test_diesel_extra_litres_above_30():
    assert fuel_bill("diesel", 60, "silver") == 3360


# =====================================
# 4. PUMP ALLOWED - FLEET BRANCHES
# =====================================

def test_fleet_within_limit():
    assert pump_allowed(150, 3, True) is True


def test_fleet_at_limit():
    assert pump_allowed(200, 3, True) is True


def test_fleet_exceeds_limit():
    assert pump_allowed(201, 3, True) is False


# =====================================
# 5. PUMP ALLOWED - NON-FLEET BRANCHES
# =====================================

def test_non_fleet_within_limit():
    assert pump_allowed(30, 1, False) is True


def test_non_fleet_at_60_litres():
    assert pump_allowed(60, 1, False) is True


def test_non_fleet_exceeds_60_litres():
    assert pump_allowed(61, 1, False) is False


def test_non_fleet_multiple_containers():
    assert pump_allowed(30, 2, False) is False


# =====================================
# 6. SESSION STATUS - PAYMENT BRANCHES
# =====================================

def test_card_payment():
    assert session_status(60, True, False) == "active"


def test_cash_payment():
    assert session_status(30, False, False) == "active"


# =====================================
# 7. SESSION STATUS - NIGHT BRANCH
# =====================================

def test_night_session():
    assert session_status(90, True, True) == "active"


def test_night_session_warning():
    assert session_status(80, True, True) == "warning"


def test_night_session_timed_out():
    assert session_status(74, True, True) == "timed_out"


# =====================================
# 8. SESSION STATUS - RESULT BRANCHES
# =====================================

def test_active_status():
    assert session_status(60, True, False) == "active"


def test_warning_status():
    assert session_status(50, True, False) == "warning"


def test_timed_out_status():
    assert session_status(44, True, False) == "timed_out"
