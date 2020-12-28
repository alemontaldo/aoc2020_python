# day 9 (~25 min)
from typing import List


def main():
    with open('input9.txt', 'r') as f:
        data: List[int] = [int(s) for s in f.read().split('\n')]

    preamble, invalid_number = 25, -1
    for i in range(preamble, len(data)):
        if not is_valid(data, i, preamble):
            invalid_number = data[i]
            break

    print('day 9a solution:')
    print(invalid_number)

    try:
        for i in range(len(data) - 1):
            contiguous = []
            j = 0
            while sum(contiguous) < invalid_number:
                contiguous.append(data[i + j])
                j = j + 1
                if sum(contiguous) == invalid_number:
                    raise BreakoutException
    except BreakoutException:
        pass

    print('day 9b solution:')
    print(min(contiguous) + max(contiguous))


def is_valid(num, i, preamble):
    for j in range(preamble):
        for k in range(j + 1, preamble):
            if num[i] == num[i-preamble:i][j] + num[i-preamble:i][k]:
                return True
    return False


class BreakoutException(BaseException):
    pass


if __name__ == "__main__":
    main()
