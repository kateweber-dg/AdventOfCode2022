
import pathlib
import sys
import string


def calculate_priority(item_list):
    priorities = [string.ascii_letters.index(x) + 1 for x in item_list]
    return priorities

def parse(puzzle_input):
    """Parse input."""
    output = puzzle_input.split('\n')
    return output

def part1(data):
    """Solve part 1."""
    splits = []
    for row in data:
        split_point = len(row) // 2
        splits.append([row[0:split_point], row[split_point:]])

    overlap = [set(row[0]).intersection(set(row[1])) for row in splits]
    overlap = [list(s)[0] for s in overlap]
    priorities = calculate_priority(overlap)
    return sum(priorities)


def part2(data):
    """Solve part 2."""
    overlap = []
    for i in range(0, len(data), 3):
        overlap.append(list(set(data[i]) & set(data[i+1]) & set(data[i+2]))[0])
    priorities = calculate_priority(overlap)
    return sum(priorities)

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

