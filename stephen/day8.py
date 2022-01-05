import itertools


def process_input(filename):
    values = []
    with open(filename) as f:
        for line in f:
            input = []
            output = []
            l = line.strip().split("|")
            for digit in l[0].strip().split(" "):
                if len(digit) == 0:
                    continue
                input.append(sorted(digit.strip()))

            for output_digit in l[1].split(" "):
                if len(output_digit) == 0:
                    continue
                output.append(sorted(output_digit.strip()))
            values.append({"input": input, "output": output})

    return values

def part1():
    values = process_input("day8-input.txt")
    count = 0

    for value in values:
        for output_digit in value["output"]:
            if len(output_digit) in [2, 4, 3, 7]:
                count += 1

    print(count)

def check_mapping(inputs, mapping):
    five_segment = ["".join(x) for x in inputs if len(x) == 5]
    six_segment = ["".join(x) for x in inputs if len(x) == 6]
    scrambled_one = "".join([x for x in inputs if len(x) == 2][0])
    scrambled_four = "".join([x for x in inputs if len(x) == 4][0])
    scrambled_seven = "".join([x for x in inputs if len(x) == 3][0])

    solution = {
        "zero": "",
        "one": "",
        "two": "",
        "three": "",
        "four": "",
        "five": "",
        "six": "",
        "seven": "",
        "eight": "abcdefg",
        "nine": ""
    }

    # then use 1, 4, 7 to double-check mapping
    one = mapping["top_right"] + mapping["bottom_right"]
    one = "".join(sorted(one))
    if sorted(one) != sorted(scrambled_one):
        return None
    solution["one"] = one

    four = mapping["top_left"] + mapping["top_right"] + mapping["middle"] + mapping["bottom_right"]
    four = "".join(sorted(four))
    if sorted(four) != sorted(scrambled_four):
        return None
    solution["four"] = four

    seven = mapping["top_middle"] + mapping["top_right"] + mapping["bottom_right"] 
    seven = "".join(sorted(seven))
    if sorted(seven) != sorted(scrambled_seven):
        return None
    solution["seven"] = seven

    # for each from each segment list, we want to confirm that it matches one of hte possible numbers:
    # 0: all except middle
    zero = mapping["top_middle"] + mapping["top_left"] + mapping["top_right"] + mapping["bottom_left"] + mapping["bottom_right"] + mapping["bottom_middle"]
    zero = "".join(sorted(zero))
    if zero not in six_segment:
        return None
    else:
        six_segment.remove(zero)
    solution["zero"] = zero

    # 6: all except top_right
    six = mapping["top_middle"] + mapping["top_left"] + mapping["middle"] + mapping["bottom_left"] + mapping["bottom_right"] + mapping["bottom_middle"]
    six = "".join(sorted(six))
    if six not in six_segment:
        return None
    else:
        six_segment.remove(six)
    solution["six"] = six

    # 9: all except bottom left
    nine = mapping["top_middle"] + mapping["top_left"] + mapping["top_right"] + mapping["middle"] + mapping["bottom_right"] + mapping["bottom_middle"]
    nine = "".join(sorted(nine))
    if nine not in six_segment:
        return None
    else:
        six_segment.remove(nine)
    solution["nine"] = nine

    # 2: all except top left, bottom right
    two = mapping["top_middle"] +  mapping["top_right"] + mapping["middle"] + mapping["bottom_left"] + mapping["bottom_middle"]
    two = "".join(sorted(two))
    if two not in five_segment:
        return None
    else:
        five_segment.remove(two)
    solution["two"] = two

    # 3: all except top left, bottom left
    three = mapping["top_middle"] + mapping["top_right"] + mapping["middle"] + mapping["bottom_right"] + mapping["bottom_middle"]
    three = "".join(sorted(three))
    if three not in five_segment:
        return None
    else:
        five_segment.remove(three)
    solution["three"] = three

    # 5: all except top right, bottom left
    five = mapping["top_middle"] + mapping["top_left"] + mapping["middle"] + mapping["bottom_right"] + mapping["bottom_middle"]
    five = "".join(sorted(five))
    if five not in five_segment:
        return None
    else:
        five_segment.remove(five)
    solution["five"] = five

    return solution


def part2():
    values = process_input("day8-input.txt")

    str_to_int_mappings = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5", 
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    position_mapping = {
        "top_middle": "",
        "top_left": "",
        "top_right": "",
        "middle": "",
        "bottom_left": "",
        "bottom_right": "",
        "bottom_middle": ""
    }

    sum = 0

    for value in values:
        descrambled_solution = None
        # set up the dict for easier mapping
        for mapping in itertools.permutations("abcdefg"):
            position_mapping["top_middle"] = mapping[0]
            position_mapping["top_left"] = mapping[1]
            position_mapping["top_right"] = mapping[2]
            position_mapping["middle"] = mapping[3]
            position_mapping["bottom_left"] = mapping[4]
            position_mapping["bottom_right"] = mapping[5]
            position_mapping["bottom_middle"] = mapping[6]

            # check the mapping, break away if it works
            solution = check_mapping(value["input"], position_mapping)
            if solution is not None:
                descrambled_solution = solution
                break
        
        # for the four outputs, use the determined wiring to figure out the represented number
        unscrambled_outputs = []
        for output in value["output"]:
            joined_output = "".join(sorted(output))
            for number, wiring in descrambled_solution.items():
                if joined_output == wiring:
                    unscrambled_outputs.append(number)

        actual_output_value_string = ""
        for value in unscrambled_outputs:
            actual_output_value_string += str_to_int_mappings[value]

        sum += int(actual_output_value_string)

    print(sum)



if __name__ == '__main__':
    part1()
    part2()