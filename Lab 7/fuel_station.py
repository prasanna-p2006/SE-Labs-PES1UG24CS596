
import math


def parse_purchase(text):
    # Check whether the input is a string
    if not isinstance(text, str):
        return "", 0.0

    # Check whether the input contains exactly one separator
    parts = text.split(":")
    if len(parts) != 2:
        return "", 0.0

    grade, litres = parts
    grade = grade.strip()

    # Check for an empty fuel grade
    if not grade:
        return "", 0.0

    try:
        litres = float(litres)
    except (ValueError, TypeError):
        return "", 0.0

    # Reject invalid numeric values such as NaN and infinity
    if not math.isfinite(litres):
        return "", 0.0

    return grade.title(), litres


def volume_average(volumes_csv):
    # Check whether the input is a non-empty string
    if not isinstance(volumes_csv, str) or not volumes_csv.strip():
        return 0

    try:
        values = [int(r.strip()) for r in volumes_csv.split(",")]
    except (ValueError, TypeError):
        return 0

    if not values:
        return 0

    return sum(values) // len(values)


def payable_bill(text):
    # Check whether the input is a string
    if not isinstance(text, str):
        return 0.0

    # Check whether the input contains exactly one separator
    parts = text.split("|")
    if len(parts) != 2:
        return 0.0

    bill, discount = parts

    try:
        bill = float(bill)
        discount = float(discount)
    except (ValueError, TypeError):
        return 0.0

    # Reject invalid numeric values
    if not math.isfinite(bill) or not math.isfinite(discount):
        return 0.0

    total = bill * 1.18 - discount

    return max(total, 0.0)


def main():
    print("==== Running parse_purchase ====")
    user_input = input("Enter grade:litres (e.g. diesel:25): ")
    result = parse_purchase(user_input)
    print("Grade and Litres:", result)

    print("\n==== Running volume_average ====")
    user_input = input("Enter pump volumes in litres as CSV (e.g. 10,25,40): ")
    result = volume_average(user_input)
    print("Average Volume:", result)

    print("\n==== Running payable_bill ====")
    user_input = input("Enter bill|discount (e.g. 2500|100): ")
    result = payable_bill(user_input)
    print("Payable Bill:", result)


if __name__ == "__main__":
    main()
