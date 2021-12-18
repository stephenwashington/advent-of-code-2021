def part1():
    count = 0
    with open('day1-input.txt') as f:
        lines = [int(x) for x in f.readlines()]
        for index, current_depth in enumerate(lines[1:]):
            previous_depth = lines[index]
            if current_depth > previous_depth:
                count += 1
    print(f"The measurement increases {count} times for part 1")

def part2():
    count = 0
    with open('day1-input.txt') as f:
        lines = [int(x) for x in f.readlines()]
        # skip the first three lines so we can index properly
        for index in range(3, len(lines)):
            current_measurement_window = lines[index] + lines[index-1] + lines[index-2]
            previous_measurement_window = lines[index-1] + lines[index-2] + lines[index-3]
            if current_measurement_window > previous_measurement_window:
                count += 1
    print(f"The measurement window increases {count} times for part 2")


if __name__ == '__main__':
    part1()
    part2()