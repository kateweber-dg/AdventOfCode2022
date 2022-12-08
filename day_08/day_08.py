import pathlib
import sys
import numpy as np


def parse(puzzle_input):
    """Parse input."""
    output = np.array([[int(y) for y in list(x)] for x in puzzle_input.split('\n')])
    return output


def is_visible(l: np.array, location: int):
    val = l[location]
    view_right = True
    view_left = True
    left_check = location - 1
    while left_check >= 0:
        if l[left_check] >= val:
            view_left = False
            break
        left_check -= 1
    for i in range(location + 1, len(l)):
        if l[i] >= val:
            view_right = False
            break
    if not view_right and not view_left:
        return 0
    else:
        return 1

def score_view(l: np.array, val):
    score = 0
    for item in l:
        if item >= val:
            score += 1
            return score
        else:
            score += 1

    return score

def part1(parsed_input):
    """Solve part 1."""
    tree_array = parsed_input
    visible_trees = np.ones(tree_array.shape, dtype=int)
    r, c = tree_array.shape
    for row_index in range(1, r - 1):
        ew = tree_array[row_index, :]
        for col_index in range(1, c - 1):
            ns = tree_array[:, col_index]
            visible_trees[row_index, col_index] = max(is_visible(ns, row_index), is_visible(ew, col_index))

    return np.sum(visible_trees)

def part2(parsed_input):
    """Solve part 2."""
    tree_array = parsed_input
    scored_trees = np.ones(tree_array.shape, dtype=int)
    r, c = tree_array.shape
    for row_index in range(0, r):
        for col_index in range(0 , c):
            val = tree_array[row_index, col_index]
            east = score_view(tree_array[row_index, col_index+1:], val)
            west = score_view(np.flip(tree_array[row_index, 0:col_index]), val)
            north = score_view(np.flip(tree_array[0:row_index, col_index]), val)
            south = score_view(tree_array[row_index+1:, col_index], val)

            scored_trees[row_index, col_index] = north * south * east * west
    return np.max(scored_trees)
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
