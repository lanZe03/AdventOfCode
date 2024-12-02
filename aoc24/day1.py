def calculate_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for l, r in zip(left_list, right_list):
        total_distance += abs(l-r)
    return total_distance


def parse_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    left_list = []
    right_list = []
    for line in lines:
        numbers = list(map(int, line.split()))
        left_list.append(numbers[0])
        right_list.append(numbers[1])
    return left_list, right_list


def calculcate_similarity(left_list, right_list):
    sim_score = 0
    for l in left_list:
        for r in right_list:
            if (l == r):
                sim_score += l
    return sim_score


if __name__ == '__main__':
    left_list, right_list = parse_input('input.txt')
    result1 = calculate_distance(left_list, right_list)
    print(result1)

    result2 = calculcate_similarity(left_list, right_list)
    print(result2)
