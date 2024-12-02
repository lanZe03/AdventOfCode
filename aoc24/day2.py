def open_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    return lines


def parse_line(line):
    return [int(elem) for elem in line.strip().split()]


def check_report(report, increasing=True):
    for i in range(len(report) - 1):
        diff = report[i+1] - report[i]
        if (increasing and (diff <= 0 or not (1 <= diff <= 3))) or \
           (not increasing and (diff >= 0 or not (1 <= abs(diff) <= 3))):
            return False
    return True


def is_safe(report):
    return check_report(report, increasing=True) or check_report(report, increasing=False)


def is_safe_with_dampener(report):
    if is_safe(report):
        return True

    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True

    return False


def part_one(lines):
    nb_safe_reports = 0

    for line in lines:
        report = parse_line(line)

        if is_safe(report):
            nb_safe_reports += 1

    return nb_safe_reports


def part_two(lines):
    nb_safe_reports = 0

    for line in lines:
        report = parse_line(line)
        if is_safe_with_dampener(report):
            nb_safe_reports += 1

    return nb_safe_reports


if __name__ == '__main__':
    lines = open_file("input2.txt")

    print(f"Part 1: {part_one(lines)}")
    print(f"Part 2: {part_two(lines)}")
