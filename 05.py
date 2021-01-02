# day 5 (~60 min)

def main():
    with open('input5.txt', 'r') as f:
        data = [s[::-1] for s in f.read().split('\n')]
        data = [[s[:3], s[3:]] for s in data]

    seats = [[to_decimal(binary_row), to_decimal(binary_column)] for binary_column, binary_row in data]

    print('day 5, part one solution:')
    print(max([seat_id(seat) for seat in seats]))

    min_row = min([seat[0] for seat in seats])
    max_row = max([seat[0] for seat in seats])
    plane = {row: [] for row in range(min_row, max_row + 1)}
    for seat in seats:
        plane[seat[0]].append(seat[1])

    for row in range(min_row + 1, max_row):
        if len(plane[row]) != 8:
            missing_row = row
            missing_col = set.difference({0, 1, 2, 3, 4, 5, 6, 7}, set(plane[row])).pop()

    print('day 5, part two solution:')
    print(seat_id([missing_row, missing_col]))


def to_decimal(s):
    v = 0
    for i, c in enumerate(s):
        if c == 'R' or c == 'B':
            v = v + 2 ** i
    return v


def seat_id(seat):
    return seat[0] * 8 + seat[1]


if __name__ == "__main__":
    main()
