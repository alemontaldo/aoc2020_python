# day 11 (~120 min)

# Represents the following neighborhood system: (where O are neighbors of c)
#       O O O
#       O c O
#       O O O
neighborhood_relative_index = [(y, x) for y in range(-1, 2) for x in range(-1, 2)]
neighborhood_relative_index.remove((0, 0))


def main():
    data = get_data()
    num_occupied = num_free = -1
    while num_occupied + num_free != 0:
        data, num_occupied = apply_rule(data, empty_adjacent_part_1, '#')
        data, num_free = apply_rule(data, adjacent_occupied_part_1, 'L')

    print('day 11, part one solution:')
    print(count_occupied(data))

    data = get_data()
    num_occupied = num_free = -1
    while num_occupied + num_free != 0:
        data, num_occupied = apply_rule(data, empty_adjacent_part_2, '#')
        data, num_free = apply_rule(data, adjacent_occupied_part_2, 'L')

    print('day 11, part two solution:')
    print(count_occupied(data))


def fill_margin(data):
    """Adds floor in the four directions"""
    data = [['.'] + lst + ['.'] for lst in data]
    floor_line = []
    for i in range(len(data[0])):
        floor_line.append('.')
    data.insert(0, floor_line)
    data.append(floor_line)
    return data


def apply_rule(data, predicate, mark_char):
    seats = set()  # set of (y, x) positions of seats to be occupied
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            if predicate(data, y, x) and data[y][x] != '.':
                seats.add((y, x))
    return mark_seats(data, seats, mark_char)


def empty_adjacent_part_1(data, yc, xc):
    return not any(n == '#' for n in get_close_neighbors(data, yc, xc))


def adjacent_occupied_part_1(data, yc, xc, num=4):
    return sum(n == '#' for n in get_close_neighbors(data, yc, xc)) >= num


def empty_adjacent_part_2(data, yc, xc):
    return not any(n == '#' for n in get_far_neighbors(data, yc, xc))


def adjacent_occupied_part_2(data, yc, xc, num=5):
    return sum(n == '#' for n in get_far_neighbors(data, yc, xc)) >= num


def get_close_neighbors(data, yc, xc):
    global neighborhood_relative_index
    neighbors = []
    for y, x in neighborhood_relative_index:
        neighbors.append(data[yc + y][xc + x])
    return neighbors


def get_far_neighbors(data, yc, xc):
    neighbors = []
    # up
    y, x = yc - 1, xc
    while data[y][x] == '.':
        if y == 0:
            break
        y = y - 1
    neighbors.append(data[y][x])
    # up-right
    y, x = yc - 1, xc + 1
    while data[y][x] == '.':
        if y == 0 or x == len(data[0]) - 1:
            break
        y = y - 1
        x = x + 1
    neighbors.append(data[y][x])
    # right
    y, x = yc, xc + 1
    while data[y][x] == '.':
        if x == len(data[0]) - 1:
            break
        x = x + 1
    neighbors.append(data[y][x])
    # down-right
    y, x = yc + 1, xc + 1
    while data[y][x] == '.':
        if y == len(data) - 1 or x == len(data[0]) - 1:
            break
        y = y + 1
        x = x + 1
    neighbors.append(data[y][x])
    # down
    y, x = yc + 1, xc
    while data[y][x] == '.':
        if y == len(data) - 1:
            break
        y = y + 1
    neighbors.append(data[y][x])
    # down-left
    y, x = yc + 1, xc - 1
    while data[y][x] == '.':
        if y == len(data) - 1 or x == 0:
            break
        y = y + 1
        x = x - 1
    neighbors.append(data[y][x])
    # left
    y, x = yc, xc - 1
    while data[y][x] == '.':
        if x == 0:
            break
        x = x - 1
    neighbors.append(data[y][x])
    # up-left
    y, x = yc - 1, xc - 1
    while data[y][x] == '.':
        if y == 0 or x == 0:
            break
        y = y - 1
        x = x - 1
    neighbors.append(data[y][x])
    return neighbors


def mark_seats(data, seats, c):
    count = 0
    for y, x in seats:
        if data[y][x] != c:
            data[y][x] = c
            count = count + 1
    return data, count


def count_occupied(data):
    return sum([seat == '#' for row in data for seat in row])


def get_data():
    with open('input11.txt', 'r') as f:
        data = [list(s) for s in f.read().split('\n')]
        return fill_margin(data)


if __name__ == "__main__":
    main()
