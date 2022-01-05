def process_input(filename):
    lanternfish = {
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
        "1": 0,
        "0": 0
    }

    with open(filename) as f:
        lanternfish_ages = [x.strip() for x in f.readline().split(",")]
        for age in lanternfish_ages:
            lanternfish[age] += 1

    return lanternfish

def calculate_lanternfish(lanternfish, iterations):
    for _ in range(iterations):
        lanternfish = iterate_fish(lanternfish)

    return lanternfish

def iterate_fish(lanternfish):
    temp0 = lanternfish["0"]

    for i in range(0, 8):
        lanternfish[str(i)] = lanternfish[str(i+1)]

    lanternfish["6"] += temp0
    lanternfish["8"] = temp0
        
    return lanternfish

def part1():
    lanternfish = process_input("day6-input.txt")
    lanternfish = calculate_lanternfish(lanternfish, 80)

    print(f"After 80 iterations, there are {sum(lanternfish.values())} lanternfish")


def part2():
    lanternfish = process_input("day6-input.txt")
    lanternfish = calculate_lanternfish(lanternfish, 256)

    print(f"After 256 iterations, there are {sum(lanternfish.values())} lanternfish")


if __name__ == '__main__':
    part1()
    part2()