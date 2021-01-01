# day 11 (~ min)

# Represents the following neighborhood system: (where O are neighbors of c)
#       O O O
#       O c O
#       O O O
neighborhood = [(y, x) for y in range(-1, 2) for x in range(-1, 2)]
neighborhood.remove((0, 0))


def main():
    # with open('input11-dummy.txt', 'r') as f:
    with open('input11.txt', 'r') as f:
        data = [list(s) for s in f.read().split('\n')]
        data = fill_margin(data)
        # print(data[1][0])  # row 1 col 0
        # print(data)

    # data = occupy_seats(data)
    # print()
    # print(data)
    #
    # data = free_seats(data)
    # print()
    # print(data)

    num_occupied = num_free = -1
    while num_occupied + num_free != 0:
        data, num_occupied = occupy_seats(data)
        # print(data)
        data, num_free = free_seats(data)
        # print(data)

    print('day 11a solution:')
    print(count_occupied(data))

    print('day 11b solution:')


def fill_margin(data):
    """Adds floor in the four directions"""
    data = [['.'] + lst + ['.'] for lst in data]
    floor_line = []
    for i in range(len(data[0])):
        floor_line.append('.')
    data.insert(0, floor_line)
    data.append(floor_line)
    return data


def occupy_seats(data):
    seats = set()  # set of (y, x) positions of seats to be occupied
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            if empty_adjacent(data, y, x) and data[y][x] != '.':
                seats.add((y, x))
    return mark_seats(data, seats, '#')


def free_seats(data):
    seats = set()  # set of (y, x) positions of seats to be free
    for y in range(1, len(data) - 1):
        for x in range(1, len(data[0]) - 1):
            if adjacent_occupied(data, y, x, 4) and data[y][x] != '.':
                seats.add((y, x))
    return mark_seats(data, seats, 'L')


def empty_adjacent(data, yc, xc):
    # return not any([data[yc + y][xc - x] == '#' for y in range(-1, 2) for x in range(-1, 2)])
    return not any(n == '#' for n in get_neighbors(data, yc, xc))


def adjacent_occupied(data, yc, xc, num):
    # return sum([data[yc + y][xc - x] == '#' for y in range(-1, 2) for x in range(-1, 2)]) >= num
    return sum(n == '#' for n in get_neighbors(data, yc, xc)) >= num


def get_neighbors(data, yc, xc):
    global neighborhood
    neighbors = []
    for y, x in neighborhood:
        neighbors.append(data[yc + y][xc + x])
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


if __name__ == "__main__":
    main()
