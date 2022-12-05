import pathlib
import re
import sys


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
    inst_list = [[int(x) for x in y] for y in inst_list]

    return {'stack': stack_dict, 'instructions': inst_list}


def part1(parsed_input):
    """Solve part 1."""
    stacks = parsed_input['stack']
    instructions = parsed_input['instructions']

    # this kind of really explict copying was necessary to keep this function from
    # simply modifying the parsed_input list instaed of working only on the copy
    output_stacks = {k: list(v) for k, v in stacks.items()}
    for inst in instructions:
        quantity = inst[0]
        fr_s = inst[1]
        to_s = inst[2]

        for q in range(quantity):
            box = output_stacks[fr_s].pop()
            output_stacks[to_s].append(box)

    answer = ''.join([output_stacks[x][-1] for x in output_stacks])
    return answer


def part2(parsed_input):
    """Solve part 2."""
    stacks = parsed_input['stack']
    instructions = parsed_input['instructions']

    # this kind of really explict copying was necessary to keep this function from
    # simply modifying the parsed_input list instaed of working only on the copy
    output_stacks = {k: list(v) for k, v in stacks.items()}

    for inst in instructions:
        quantity = inst[0]
        fr_s = inst[1]
        to_s = inst[2]

        boxes = output_stacks[fr_s][-1 * quantity:]
        output_stacks[fr_s] = output_stacks[fr_s][: -1 * quantity]
        output_stacks[to_s].extend(boxes)
    answer = ''.join([output_stacks[x][-1] for x in output_stacks])
    return answer


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
