# day 8 (~30 min)

def main():
    with open('input8.txt', 'r') as f:
        cmd = [[s.split()[0], int(s.split()[1][1:])*(-1 if s.split()[1][:1] == '-' else 1)] for s in f.read().split('\n')]

    print('day 8a solution:')
    acc, pc = run(cmd)
    print(acc)

    for i in range(len(cmd)):
        cmd = change_instruction(cmd, i)
        acc, pc = run(cmd)
        cmd = change_instruction(cmd, i)
        if pc == len(cmd):
            break

    print('day 8b solution:')
    print(acc)


def run(cmd):
    acc = pc = 0
    end_flag = False
    visited_location = set()
    visited_location.add(0)

    while not end_flag:
        if cmd[pc][0] == 'acc':
            acc = acc + cmd[pc][1]
            pc = pc + 1
        elif cmd[pc][0] == 'jmp':
            pc = pc + cmd[pc][1]
        else:
            pc = pc + 1

        old_len = len(visited_location)
        visited_location.add(pc)
        end_flag = old_len == len(visited_location) or pc == len(cmd)
    return acc, pc


def change_instruction(cmd, i):
    if cmd[i][0] != 'acc':
        cmd[i][0] = 'jmp' if cmd[i][0] == 'nop' else 'nop'
    return cmd


if __name__ == "__main__":
    main()
