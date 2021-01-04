# day 11 (~120 min)


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


def apply_rule(data, predicate, mark_char):
    seats = set()  # set of (y, x) positions of seats to be occupied
    for y in range(len(data)):
        for x in range(len(data[0])):
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
    neighbors = []
    num_rows, num_cols = len(data), len(data[0])
    for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        y, x = yc + dy, xc + dx
        if 0 <= y < num_rows and 0 <= x < num_cols:
            neighbors.append(data[y][x])
    return neighbors


def get_far_neighbors(data, yc, xc):
    neighbors = []
    num_rows, num_cols = len(data), len(data[0])
    for dy, dx in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        y, x = yc + dy, xc + dx
        while 0 <= y < num_rows and 0 <= x < num_cols:
            if data[y][x] != '.':
                neighbors.append(data[y][x])
                break
            y += dy
            x += dx
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
        return [list(s) for s in f.read().splitlines()]


if __name__ == "__main__":
    main()
