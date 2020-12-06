# day 6 (~20 min)

def main():
    with open('input6.txt', 'r') as f:
        groups = [s.split('\n') for s in f.read().split('\n\n')]

    answers = [create_set_1(group) for group in groups]

    print('day 6a solution:')
    print(sum([len(ans) for ans in answers]))

    answers = [create_set_2(group) for group in groups]

    print('day 6b solution:')
    print(sum([len(ans) for ans in answers]))


def create_set_1(group):
    ans = set()
    for person in group:
        for letter in person:
            ans.add(letter)
    return ans


def create_set_2(group):
    ans_per_person = []
    for person in group:
        ans = set()
        for letter in person:
            ans.add(letter)
        ans_per_person.append(ans)

    return set.intersection(*ans_per_person)


if __name__ == "__main__":
    main()
