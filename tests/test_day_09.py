import pathlib

import pytest
import numpy as np
import day_09.day_09 as aoc


PUZZLE_DIR = pathlib.Path(__file__).parent.parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "day_09/example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)
@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "day_09/example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [['R', 4], ['U', 4], ['L', 3], ['D', 1], ['R', 4], ['D', 1], ['L', 5], ['R', 2]]

def test_move_head(example1):
    head = aoc.Knot()
    for instruction in example1:
        for repeat in range(instruction[1]):
            head.move(instruction[0])

    assert head.x == 2
    assert head.y == 2

def test_follow_head():

    for dir in ['U', 'D', 'L', 'R']:
        for pos in [(0, 1), (1, 1), (1, 0), (1, -1),
                    (0, -1), (-1, -1), (-1, 0), (-1, 1)]:
            head = aoc.Knot(0, 0)
            tail = aoc.Knot(x=pos[0], y=pos[1])
            head.move(dir)
            tail.follow(head)
            print(tail)

    return

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 13

def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1)== 1

def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == 36



