# day 2 (~35 min tot the bad version)

def main():
    with open('input2.txt', 'r') as f:
        # ----> my first parsing I did for the solutions that index elements in lists
        #line = f.read().split('\n')
        # minVal = [int(i.split(':')[0].split(' ')[0].split('-')[0]) for i in line]
        # maxVal = [int(i.split(':')[0].split(' ')[0].split('-')[1]) for i in line]
        # letter = [i.split(':')[0].split(' ')[1] for i in line]
        # passw = [i.split(':')[1][1:] for i in line]

        # a parsing that reduces code repetition and uses naming
        policy_and_passw = [i.split(':') for i in f.read().split('\n')]
        passw = [i[1][1:] for i in policy_and_passw]   # [1:] is for discarding first char which is a blank space
        numbers_and_letter = [i[0].split(' ') for i in policy_and_passw]
        letter = [i[1] for i in numbers_and_letter]
        numbers = [i[0].split('-') for i in numbers_and_letter]
        num_1 = [int(i[0]) for i in numbers]
        num_2 = [int(i[1]) for i in numbers]

    #  ----> indexing elements in lists (blah and dreadful performance)
    # count = 0
    # for i in range(len(passw)):
    #     if passw[i].count(letter[i]) >= minVal[i] and passw[i].count(letter[i]) <= maxVal[i]:
    #         count = count + 1

    #  here we are...
    count = len([p for p, l, m, M in zip(passw, letter, num_1, num_2) if p.count(l) in range(m, M + 1)])

    print('day 2, part one solution:')
    print(count)

    #  ----> indexing elements in lists (blah and dreadful performance)
    # count = 0
    # for i in range(len(passw)):
    #     if len(passw[i]) > minVal[i] - 1 and len(passw[i]) > maxVal[i] - 1:
    #         if (passw[i][minVal[i] - 1] == letter[i]) != (passw[i][maxVal[i] - 1] == letter[i]):
    #             count = count + 1

    #  here we are...
    count = len([p for p, l, p1, p2 in zip(passw, letter, num_1, num_2) if is_valid_part_2(p, l, p1, p2)])

    print('day 2, part two solution:')
    print(count)


def is_valid_part_2(p, l, p1, p2):
    if len(p) > p1 - 1 and len(p) > p2 - 1:
        if (p[p1 - 1] == l) != (p[p2 - 1] == l):
            return True
    return False


if __name__ == "__main__":
    main()
