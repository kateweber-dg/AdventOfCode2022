import pathlib
import re
import sys

def locate_nonrepeating_pattern(parsed_input, pattern_length=4):
    scores = []
    for row in parsed_input:
        for ix in range(pattern_length, len(row)):
            test = row[ix - pattern_length: ix]
            if len(set(test)) == pattern_length:
                scores.append(ix)

                break
    return scores

def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')
    return lines


def part1(parsed_input):
    """Solve part 1."""
    return locate_nonrepeating_pattern(parsed_input, 4)

def part2(parsed_input):
    """Solve part 2."""
    return locate_nonrepeating_pattern(parsed_input, 14)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
