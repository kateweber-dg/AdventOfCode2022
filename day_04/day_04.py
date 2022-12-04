
import pathlib
import sys
import string


def calculate_priority(item_list):
    priorities = [string.ascii_letters.index(x) + 1 for x in item_list]
    return priorities

def parse(puzzle_input):
    """Parse input."""
    lines = [x.split(',') for x in puzzle_input.split('\n')]
    output = []
    for pair in lines:
        pair = [x.split(',') for x in pair]
        for index, zone in enumerate(pair):
            ends = zone[0].split('-')
            pair[index] = set(range(int(ends[0]), int(ends[1])+1))
        output.append(pair)
    return output

def part1(data):
    """Solve part 1."""
    subsets = [1 for x in data if (x[0].issubset(x[1]) or (x[1].issubset(x[0])))]
    return sum(subsets)


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
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))

