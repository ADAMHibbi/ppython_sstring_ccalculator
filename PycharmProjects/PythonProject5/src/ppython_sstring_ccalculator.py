def python_add(numbers: str) -> int:
    if numbers == "":
        return 0

    if numbers.isdigit():
        return int(numbers)

    parts = numbers.split(",")
    total = 0
    for part in parts:
        total += int(part)
    return total

