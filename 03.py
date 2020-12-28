# day 3 (~30 min)

def main():
    with open('input3.txt', 'r') as f:
        lines = f.read().split('\n')

    print('day 3a solution:')
    print(count_trees(3, lines))

    print('day 3b solution:')
    print(count_trees(1, lines)
          * count_trees(3, lines)
          * count_trees(5, lines)
          * count_trees(7, lines)
          * count_trees(1, lines, slope_y=2))


def count_trees(slope_x, lines, slope_y=1):
    x = 0
    line_length = len(lines[0])
    count = 0
    for y in range(0, len(lines), slope_y):
        if lines[y][x] == '#':
            count = count + 1
        x = (x + slope_x) % line_length
    return count


if __name__ == "__main__":
    main()
