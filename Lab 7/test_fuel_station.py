
from hypothesis import given, strategies as st
from hypothesis import assume
import pytest

from fuel_station import parse_purchase, volume_average, payable_bill


# --------------------------------------------------
# 1. FUZZ TEST: parse_purchase()
# --------------------------------------------------

@given(st.text() | st.none())
def test_parse_purchase_no_crash(s):
    try:
        parse_purchase(s)
    except Exception as e:
        assert False, f"parse_purchase crashed with input {s!r}: {e}"


# --------------------------------------------------
# 2. FUZZ TEST: volume_average()
# --------------------------------------------------

@given(st.text() | st.none())
def test_volume_average_no_crash(s):
    try:
        volume_average(s)
    except Exception as e:
        assert False, f"volume_average crashed with input {s!r}: {e}"


# --------------------------------------------------
# 3. FUZZ TEST: payable_bill()
# --------------------------------------------------

@given(st.text() | st.none())
def test_payable_bill_no_crash(s):
    try:
        payable_bill(s)
    except Exception as e:
        assert False, f"payable_bill crashed with input {s!r}: {e}"


# --------------------------------------------------
# 4. VALID INPUT PROPERTY TESTS
# --------------------------------------------------

# Test valid fuel purchase inputs
@given(
    st.text(
        alphabet=st.characters(whitelist_categories=("Lu", "Ll")),
        min_size=1
    ),
    st.floats(
        min_value=0,
        max_value=1000000,
        allow_nan=False,
        allow_infinity=False
    )
)
def test_parse_purchase_valid(grade, litres):
    result = parse_purchase(f"{grade}:{litres}")

    assert result[0] == grade.strip().title()
    assert result[1] == pytest.approx(litres)


# Test valid pump volume CSV inputs
@given(st.lists(st.integers(), min_size=1, max_size=20))
def test_volume_average_valid(volumes):
    csv_input = ",".join(str(v) for v in volumes)

    result = volume_average(csv_input)

    expected = sum(volumes) // len(volumes)

    assert result == expected


# Test valid bill calculation inputs
@given(
    st.floats(
        min_value=0,
        max_value=1000000,
        allow_nan=False,
        allow_infinity=False
    ),
    st.floats(
        min_value=0,
        max_value=1000000,
        allow_nan=False,
        allow_infinity=False
    )
)
def test_payable_bill_valid(bill, discount):
    result = payable_bill(f"{bill}|{discount}")

    expected = max(bill * 1.18 - discount, 0)

    assert result == pytest.approx(expected)
    assert result >= 0
