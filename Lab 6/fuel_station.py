VOUCHER_LITRES = {"regular": 10, "premium": 15, "diesel": 20}


def fuel_bill(grade, litres, loyalty_tier):
    if grade not in VOUCHER_LITRES:
        raise ValueError("unknown fuel grade")
    if litres < 0:
        raise ValueError("invalid litres")
    covered = VOUCHER_LITRES[grade]
    if loyalty_tier == "gold" and grade != "diesel":
        covered += 5
    extra = litres - covered
    if extra <= 0:
        return 0
    if grade == "diesel":
        rate = 90
    else:
        rate = 105
    if extra > 30:
        rate = rate - 6
        if loyalty_tier == "gold":
            rate -= 4
    return extra * rate


def pump_allowed(litres_requested, containers, is_fleet):
    if is_fleet:
        return litres_requested <= 200
    if litres_requested > 60:
        return False
    return containers <= 1


def session_status(seconds_left, is_card_payment, is_night):
    if is_card_payment:
        cutoff = 60
    else:
        cutoff = 30
    if is_night:
        cutoff += 30
    if seconds_left >= cutoff:
        return "active"
    elif seconds_left >= cutoff - 15:
        return "warning"
    return "timed_out"
