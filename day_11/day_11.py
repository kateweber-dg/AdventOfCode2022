import pathlib
import sys
from collections import deque
import re


class Monkey(object):
    def __init__(self, name):
        self.name = name
        self.operation = None
        self.items = deque()
        self.test_value = None
        self.true_monkey = None
        self.false_monkey = None
        self.inspection_count = 0

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def operation_mapper(self, operation_string):
        if operation_string == '+':
            return self.add
        elif operation_string ==  '*':
            return self.multiply
        else:
            return 'error'

    def operate(self, value):
        if self.operation[0] == 'old':
            a = value
        else:
            a = int(self.operation[0])

        if self.operation[2] == 'old':
            b = value
        else:
            b = int(self.operation[2])

        return self.operation_mapper(operation_string=self.operation[1])(a, b)

    def boredom(self, item):
        return item // 3

    def test_worry(self, item):
        return item % self.test_value == 0

    def __repr__(self):
        return f'{self.name} - {self.items}'


def parse(puzzle_input):
    """Parse input."""
    output = []
    monkey_input = [x.split('\n') for x in puzzle_input.split('Monkey ')[1:]]
    for monkey_data in monkey_input:
        new_monkey = Monkey(name=monkey_data[0][0])
        new_monkey.items = deque([int(x) for x in re.findall(r'\d.', monkey_data[1])])
        operation_text = re.search('=\s(\w+)\s([+*])\s(\w+)', monkey_data[2])
        new_monkey.operation = [operation_text[x] for x in range(1, 4)]
        new_monkey.test_value = int(re.findall(r'\d+', monkey_data[3])[0])
        new_monkey.true_monkey = int(re.findall(r'\d+', monkey_data[4])[0])
        new_monkey.false_monkey = int(re.findall(r'\d+', monkey_data[5])[0])
        output.append(new_monkey)

    return output


def part1(parsed_input):
    """Solve part 1."""
    monkeys = parsed_input
    rounds = 10001
    for round in range(1, rounds):
        for monkey in monkeys:
            while len(monkey.items) > 0:
                item = monkey.items.popleft()
                monkey.inspection_count += 1
                inspected_value = monkey.operate(item)
                # bored_value = monkey.boredom(inspected_value)
                bored_value = inspected_value
                if monkey.test_worry(bored_value):
                    monkeys[monkey.true_monkey].items.append(bored_value)
                else:
                    monkeys[monkey.false_monkey].items.append(bored_value)

    inspection_counts = [m.inspection_count for m in monkeys]
    inspection_counts.sort()

    return inspection_counts[-1] * inspection_counts[-2]

def part2(parsed_input):
    """Solve part 2."""
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input: str = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
