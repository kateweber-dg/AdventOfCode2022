import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""
    i = 0
    output = [0]

    for row in puzzle_input.split('\n'):
        try:
            n = int(row.strip())
            output[i] += n
        except ValueError:
            i += 1
            output.append(0)
    output.sort()
    return output

def part1(data):
    """Solve part 1."""
    max_calories = data[-1]
    return max_calories

def part2(data):
    """Solve part 2."""
    top_3_calories =  sum(data[-3:])
    return top_3_calories

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

