def part1():
    with open("day2-input.txt") as f:
        horizontal_position = 0
        depth = 0
        for line in f:
            l = line.split(" ")
            direction = l[0]
            magnitude = int(l[1])

            if direction == "forward":
                horizontal_position += magnitude
            elif direction == "up":
                depth -= magnitude
            elif direction == "down":
                depth += magnitude

    print(f"Final position: {horizontal_position} x {depth} = {horizontal_position*depth}")

def part2():
    with open("day2-input.txt") as f:
        horizontal_position = 0
        depth = 0
        aim = 0
        for line in f:
            l = line.split(" ")
            direction = l[0]
            magnitude = int(l[1])

            if direction == "forward":
                horizontal_position += magnitude
                depth += aim*magnitude
            elif direction == "up":
                aim -= magnitude
            elif direction == "down":
                aim += magnitude

    print(f"Final position: {horizontal_position} x {depth} = {horizontal_position*depth}")


if __name__ == '__main__':
    part1()
    part2()