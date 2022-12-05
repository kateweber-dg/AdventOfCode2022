
import pathlib
import sys
import re

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n\n')
    stacks = lines[0].split('\n')
    instructions = lines[1].split('\n')

    # get the stacks
    stack_dict = {}
    stack_labels = [int(x) for x in re.findall('\d', stacks.pop())]

    for label in stack_labels:
        stack_dict[label] = []

    row = stacks.pop()
    while True:
        for label in stack_labels:
            col_index = ((label - 1) * 4) + 1
            if row[col_index] == ' ':
                continue
            else:
                stack_dict[label].append(row[col_index])
        if len(stacks) == 0:
            break
        else:
            row = stacks.pop()

    # get the instructions

    inst_list = [re.findall('\d+', x) for x in instructions]

    return stack_dict, inst_list

def part1(data):
    """Solve part 1."""

    stacks, instructions = data

    return 'CMZ'


def part2(data):
    """Solve part 2."""
    intersections = [1 for x in data if len(x[0] & x[1]) > 0]
    return sum(intersections)

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))

