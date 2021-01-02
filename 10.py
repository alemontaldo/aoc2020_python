# day 10 (~90 min)

def main():
    with open('input10.txt', 'r') as f:
        data = list(map(int, f.read().split('\n')))
        data.sort()
        data.insert(0, 0)
        data.append(max(data) + 3)

    ans = [i for i in [data[i + 1] - data[i] for i in range(len(data) - 1)]]

    print('day 10, part one solution:')
    print(ans.count(1) * ans.count(3))

    # nodes are traversed backwards while propagating the number of new possible paths
    path_from = {i: 1 for i in data}
    for i in reversed(range(len(data) - 1)):
        new_paths = 0
        for j in range(1, 4):
            new_paths = new_paths + (path_from[data[i] + j] if data[i] + j in path_from else 0)
        path_from[data[i]] = new_paths

    print('day 10, part two solution:')
    print(path_from[0])


if __name__ == "__main__":
    main()
