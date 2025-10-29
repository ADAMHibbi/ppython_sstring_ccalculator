def python_add(numbers: str) -> int:
    if numbers == "":
       return 0
    if numbers.isdigit():
       return int(numbers)
