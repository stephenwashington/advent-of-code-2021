def process_input(filename):
    smoke_map = []
    with open(filename) as f:
        for line in f:
            row = []
            for char in line.strip():
                row.append(int(char))
            smoke_map.append(row)
    return smoke_map

def section_is_higher(smoke_map, center, adjacent):
    """ True if the adjacent section is higher than the center (the point we're evaluating)"""
    if adjacent is None:
        return True
    else:
        return smoke_map[adjacent[0]][adjacent[1]] > center


def part1():
    smoke_map = process_input("day9-input.txt")
    count = 0
    for row_idx in range(len(smoke_map)):
        for col_idx in range(len(smoke_map[0])):
            location = smoke_map[row_idx][col_idx]
            left = (row_idx, col_idx-1) if col_idx != 0 else None
            right = (row_idx, col_idx+1) if col_idx != len(smoke_map[0])-1 else None
            up = (row_idx-1, col_idx) if row_idx != 0 else None
            down = (row_idx+1, col_idx) if row_idx != len(smoke_map)-1 else None

            if section_is_higher(smoke_map, location, up) and \
               section_is_higher(smoke_map, location, down) and \
               section_is_higher(smoke_map, location, left) and \
               section_is_higher(smoke_map, location, right):
               count += (location + 1) #add 1 because of risk level

    print(count)
            

def part2():
    smoke_map = process_input("day9-input.txt")
    basin_low_points = []

    for row_idx in range(len(smoke_map)):
        for col_idx in range(len(smoke_map[0])):
            location = smoke_map[row_idx][col_idx]
            left = (row_idx, col_idx-1) if col_idx != 0 else None
            right = (row_idx, col_idx+1) if col_idx != len(smoke_map[0])-1 else None
            up = (row_idx-1, col_idx) if row_idx != 0 else None
            down = (row_idx+1, col_idx) if row_idx != len(smoke_map)-1 else None

            if section_is_higher(smoke_map, location, up) and \
               section_is_higher(smoke_map, location, down) and \
               section_is_higher(smoke_map, location, left) and \
               section_is_higher(smoke_map, location, right):
               basin_low_points.append((row_idx, col_idx))

    areas = []
    for low_point in basin_low_points:
        #print(f"Current low point {low_point}")
        #for x in range(len(smoke_map)):
        #    for y in range(len(smoke_map[0])):
        #        print(f"{smoke_map[x][y]} ", end="")
        #    print()
        area = 0
        cells_to_analyze = [low_point]
        while cells_to_analyze:
            current_cell = cells_to_analyze.pop() # pop the top of the stack
            #print(f"Current cell: {current_cell}")
            #print(current_cell)
            row_idx = current_cell[0]
            col_idx = current_cell[1]

            left = (row_idx, col_idx-1) if col_idx != 0 else None
            right = (row_idx, col_idx+1) if col_idx != len(smoke_map[0])-1 else None
            up = (row_idx-1, col_idx) if row_idx != 0 else None
            down = (row_idx+1, col_idx) if row_idx != len(smoke_map)-1 else None

            if smoke_map[current_cell[0]][current_cell[1]] != 9 and smoke_map[current_cell[0]][current_cell[1]] != "X":
                area += 1
                smoke_map[row_idx][col_idx] = "X" #cell has been visited
            
            if left is not None:
                if smoke_map[left[0]][left[1]] != 9 and smoke_map[left[0]][left[1]] != "X":
                    #print(f"{smoke_map[left[0]][left[1]]} append left {left}")
                    cells_to_analyze.append(left)
            if right is not None:
                if smoke_map[right[0]][right[1]] != 9 and smoke_map[right[0]][right[1]] != "X":
                    #print(f"{smoke_map[right[0]][right[1]]} append right {right}")
                    cells_to_analyze.append(right)
            if up is not None:
                if smoke_map[up[0]][up[1]] != 9 and smoke_map[up[0]][up[1]] != "X":
                    #print(f"{smoke_map[up[0]][up[1]]} append up {up} ")
                    cells_to_analyze.append(up)
            if down is not None:
                if smoke_map[down[0]][down[1]] != 9 and smoke_map[down[0]][down[1]] != "X":
                    #print(f"{smoke_map[down[0]][down[1]]} append down {down}")
                    cells_to_analyze.append(down)

        areas.append(area)
    areas = sorted(areas)
    top_three = areas[-3:]
    print(top_three[0]*top_three[1]*top_three[2])

if __name__ == '__main__':
    part1()
    part2()