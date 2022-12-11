import pathlib

import pytest
import numpy as np
import day_10.day_10 as aoc


PUZZLE_DIR = pathlib.Path(__file__).parent.parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "day_10/example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "day_10/example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [['noop'], ['addx', 3], ['addx', -5]]

def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc.part1(example2) == 13140

def test_part2_example1(example1):
    """Test part 2 on example input."""
    pass

def test_part2_example2(example2):
    """Test part 2 on example input."""
    pass



