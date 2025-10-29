def python_add(numbers: str) -> int:
    if numbers == "":
        return 0

    if numbers.isdigit():
        return int(numbers)

    if "," in numbers:
        parts = numbers.split(",")
        if len(parts) == 2:
            return int(parts[0]) + int(parts[1])
