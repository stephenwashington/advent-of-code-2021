import math

def process_input(filename):
    lines = []
    with open(filename) as f:
        for line in f:
            start_and_end = line.strip().split(" -> ")
            start = [int(x) for x in start_and_end[0].split(",")]
            end = [int(x) for x in start_and_end[1].split(",")]
            lines.append([start, end])

    x_max = 0
    y_max = 0
    for line in lines:
        start, end = line[0], line[1]
        x_max = max(x_max, start[0], end[0])
        y_max = max(y_max, start[1], end[1])
    #print(x_max, y_max)
    return lines, x_max, y_max

def distance(point1, point2):
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    return math.sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1) )

def is_point_on_line(start, end, point):
    return distance(start, point) + distance(end, point) - distance(start, end) < 0.0001

def generate_blank_grid(x_max, y_max):
    grid = []
    for x in range(x_max+1):
        row = []
        for y in range(y_max+1):
            row.append(0)
        grid.append(row)

    return grid

def is_diagonal(start, end):
    return start[0] != end[0] and start[1] != end[1]

def find_intersections(skip_diagonals):
    lines, x_max, y_max = process_input("day5-input.txt")
    grid = generate_blank_grid(x_max, y_max)

    for line in lines:
        start, end = line[0], line[1]
        if skip_diagonals and is_diagonal(start, end):
            continue
        
        x_lower = min(start[0], end[0])
        x_upper = max(start[0], end[0])+1
        y_lower = min(start[1], end[1])
        y_upper = max(start[1], end[1])+1
        #print(line, x_lower, x_upper, y_lower, y_upper)
        for x in range(x_lower, x_upper):
            for y in range(y_lower, y_upper):
                point = [x,y]
                if is_point_on_line(start, end, point):
                    grid[x][y] += 1


    solution = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] > 1:
                solution += 1

    return solution

def part1():
    solution = find_intersections(True)
    print(f"Ignoring intersections, there are {solution} points of intersection in the grid")


def part2():
    # This takes about 4 minutes to run! Probably a better way to do this
    # Involving the fact that all lines are diagonal on 45 degrees
    # meaning points increment at same pace
    # slowness comes from calculating distance of so many points for each diagonal
    solution = find_intersections(False)
    print(f"Including intersections, there are {solution} points of intersection in the grid")


if __name__ == '__main__':
    part1()
    part2()