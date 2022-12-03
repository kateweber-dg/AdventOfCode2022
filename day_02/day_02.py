
import pathlib
import sys

win_table = [[3, 6, 0],
             [0, 3, 6],
             [6, 0, 3]]

def parse(puzzle_input):
    """Parse input."""
    output = []
    for row in puzzle_input.split('\n'):
        output.append(row.split())
    return output

def part1(data):
    """Solve part 1."""

    indices = {"X": 0, "Y": 1, "Z": 2, "A": 0, "B": 1, "C": 2}

    score = 0
    for row in data:
        round_score = win_table[indices[row[0]]][indices[row[1]]] + indices[row[1]] + 1
        score += round_score

    return score

def part2(data):
    """Solve part 2."""

    indices = {"X": 0, "Y": 3, "Z": 6, "A": 0, "B": 1, "C": 2}

    score = 0

    for row in data:
        desired_index = win_table[indices[row[0]]].index(indices[row[1]])
        score = score + desired_index + 1 + indices[row[1]]
    return score

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

