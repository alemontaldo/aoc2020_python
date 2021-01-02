# day 7 (~1h 15')

def main():
    with open('input7.txt', 'r') as f:
        bag_and_rule = [s.split() for s in f.read().split('\n')]
        E, V = set(), set()  # edges and vertices of the graph
        for i in bag_and_rule:
            E, V = add_in_graph(i, E, V)

    explored, old = {'shiny gold'}, {}
    while set.difference(explored, old) != set():
        old = explored.copy()
        for dest_bag in old:
            for rule in E:
                if rule[1] == dest_bag and rule[0] not in explored:
                    explored.add(rule[0])

    print('day 7, part one solution:')
    print(len(explored)-1)

    print('day 7, part two solution:')
    print(num_bags_required_2('shiny gold', E))


def add_in_graph(words, E, V):
    bag, rules = format_line(words)
    V.add(bag)
    for rule in rules:
        E.add((bag, rule[1], int(rule[0])))

    return E, V


def format_line(words):
    bag = words[0] + ' ' + words[1]
    num_bags_contained = (len(words) - 4) // 4
    return bag, [(words[4 * i], words[4 * i + 1] + ' ' + words[4 * i + 2]) for i in range(1, num_bags_contained + 1)]


def num_bags_required_2(bag, E):
    if bag_is_empty(bag, E):
        return 0
    else:
        inside = [(e[1], e[2]) for e in E if e[0] == bag]
        return sum([bag_and_num[1] + bag_and_num[1] * num_bags_required_2(bag_and_num[0], E) for bag_and_num in inside])


def bag_is_empty(bag, E):
    return not any([bag == e[0] for e in E])


if __name__ == "__main__":
    main()
