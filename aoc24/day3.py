import re


def open_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    string = ''.join(map(str, lines))

    return string


def calculate_mul_sum(string):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    matches = re.findall(pattern, string)

    sum = 0

    for match in matches:
        numbers = re.findall(r"\d{1,3}", match)

        if len(numbers) == 2:  # Valid mul(X, Y) must have exactly two numbers
            x, y = map(int, numbers)
            sum += x * y

    return sum


def calculate_conditional_mul_sum(string):
    instructions_pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"

    instructions = re.findall(instructions_pattern, string)

    enabled = True
    sum = 0

    for instruction in instructions:
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False
        elif instruction.startswith("mul(") and enabled:
            numbers = re.findall(r"\d{1,3}", instruction)
            if len(numbers) == 2:
                x, y = map(int, numbers)
                sum += x * y

    return sum


def part_one(string):
    return calculate_mul_sum(string)


def part_two(lines):
    return calculate_conditional_mul_sum(lines)


if __name__ == '__main__':
    instructions = open_file("input3.txt")

    print(f"Part 1: {part_one(instructions)}")
    print(f"Part 2: {part_two(instructions)}")
