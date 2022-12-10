import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    output = [x.split(' ') for x in puzzle_input.split('\n')]
    output = [[x[0], int(x[1])] for x in output]
    return output

def part1(parsed_input):
    """Solve part 1."""
    pass


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
