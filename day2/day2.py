
import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    output = {}
    for play in puzzle_input.split('\n'):
        vals = play.split(' ')
        output[vals[0]] = vals[1]
    return output

def part1(data):
    """Solve part 1."""
    win_table = [[3, 6, 0],
                 [0, 3, 6],
                 [6, 0, 3]]
    values = {"X": 1, "Y": 2, "Z": 3}
    return 15

def part2(data):
    """Solve part 2."""

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

