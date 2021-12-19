def get_zero_and_one_count(lines, column):
    zero_count = 0
    one_count = 0
    for line in lines:
        char = line[column]
        if char == "0":
            zero_count += 1
        elif char == "1":
            one_count += 1    
    return zero_count, one_count

def filter_lines(lines, column, bit_to_keep, bit_to_drop):
    """Filtering is where we get the zero and one count
       Then we keep the lines that have the more (or less ) common bit, based on the rule
    """
    zero_count, one_count = get_zero_and_one_count(lines, column)

    newlines = []
    if one_count >= zero_count:
        for line in lines:
            if line[column] == bit_to_keep:
                newlines.append(line)
    else:
        for line in lines:
            if line[column] == bit_to_drop:
                newlines.append(line)
    
    return newlines


def get_rating(lines, bit_to_keep, bit_to_drop):
    """The keep and drop bits refer to how we determine the rating
        - for o2, we keep the lines that have the bit that's more common in each column
        - for co2, we keep the lines that have the less common bit
    """
    number_of_columns = len(lines[0].strip())
    for column in range(number_of_columns):
        lines = filter_lines(lines, column, bit_to_keep, bit_to_drop)
        if len(lines) == 1:
            break

    return lines[0]

def part1():
    gamma = ""
    epsilon = ""
    with open("day3-input.txt") as f:
        lines = f.readlines()
        number_of_columns = len(lines[0].strip())
        for column in range(number_of_columns):
            zero_count, one_count = get_zero_and_one_count(lines, column)

            gamma += "1" if one_count >= zero_count else "0"
            epsilon += "0" if one_count >= zero_count else "1"

    decimal_gamma = int(gamma, 2)
    decimal_epsilon = int(epsilon, 2)
    print(f"The power consumption rate is {decimal_gamma} ({gamma}) x {decimal_epsilon} ({epsilon}) = {decimal_gamma*decimal_epsilon }")

def part2():
    with open("day3-input.txt") as f:
        lines = [l.strip() for l in f.readlines()]
        o2_level = get_rating(lines, "1", "0")
        co2_level = get_rating(lines, "0", "1")
    
    decimal_o2_level = int(o2_level, 2)
    decimal_co2_level = int(co2_level, 2)
    print(f"The life support rating is {decimal_o2_level} ({o2_level}) x {decimal_co2_level} ({co2_level}) = {decimal_o2_level * decimal_co2_level}")


if __name__ == '__main__':
    part1()
    part2()