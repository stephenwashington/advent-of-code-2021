def process_input(filename):
    crabs = []
    with open(filename) as f:
        crabs = [int(x.strip()) for x in f.readline().split(",")]

    return crabs

def pre_calculate_fuel_usage(constant_burn, max_distance):
    fuel_usage = {}
    if constant_burn:
        for distance in range(max_distance):
            fuel_usage[str(distance)] = distance
    else:
        for distance in range(max_distance):
            fuel_usage[str(distance)] = sum([x for x in range(1, distance+1)])

    return fuel_usage

def calculate_best_position(crabs, fuel_usage):
    lowest_fuel_used = 10**15
    best_position = -1
    for position in range(1, max(crabs)):
        fuel_used = 0
        for crab_position in crabs:
            distance_to_travel = abs(crab_position - position)
            fuel_used += fuel_usage[str(distance_to_travel)]

        if fuel_used < lowest_fuel_used:
            lowest_fuel_used = fuel_used
            best_position = position

    return best_position, lowest_fuel_used

def part1():
    crabs = process_input("day7-input.txt")
    fuel_usage = pre_calculate_fuel_usage(True, max(crabs))
    best_position, lowest_fuel_used = calculate_best_position(crabs, fuel_usage)

    print(f"Assuming constant fuel burn rate, Lowest fuel used is {lowest_fuel_used}, moving to position {best_position}")

def part2():
    crabs = process_input("day7-input.txt")
    fuel_usage = pre_calculate_fuel_usage(False, max(crabs))
    best_position, lowest_fuel_used = calculate_best_position(crabs, fuel_usage)

    print(f"Assuming geometric fuel burn rate, lowest fuel used is {lowest_fuel_used}, moving to position {best_position}")


if __name__ == '__main__':
    part1()
    part2()