# day 1 (~20 min tot)

def main():
    with open('input1.txt', 'r') as f:
        data = [int(i) for i in f.read().split('\n')]

    result1 = [(a, b) for a in data for b in data if a + b == 2020]  # o(N^2)
    # result1 = [(a, 2020 - a) for a in data if (2020 - a) in data]  # again brute force

    #  --- some thought about something better performing (if well implemented)
    # data = sorted(data)  # first sort with o(NlogN)
    # N = len(data)
    # start comparing from the higher number with the difference to 2020. if you find something bigger stop
    # for i in len(data):
    #    for j in len(data - i):
    #        if data[N-j] == 2020 - data[i]:
    #      ... ...  ...
    # NOTE: double occurrences of the same number is useless (except for case 1010). these could be trimmed away

    print('day 1, part one solution:')
    assert len(result1) == 2
    a, b = result1[0]
    print(a * b)

    result2 = [(a, b, c) for a in data for b in data for c in data if a + b + c == 2020]

    print('day 1, part two solution:')
    assert len(result1) == 2
    a, b, c = result2[0]
    print(a * b * c)


if __name__ == "__main__":
    main()
