import pathlib

import pytest
import numpy as np
import day_08.day_08 as aoc


PUZZLE_DIR = pathlib.Path(__file__).parent.parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "day_08/example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1.shape == (5, 5)

def test_is_visible():
    l = np.array([6, 5, 3, 3, 2])
    ans = [aoc.is_visible(l, x) for x in [1, 2, 3]]
    assert ans == [1, 0, 1]
def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 21

def test_part2_example1(example1):
    """Test part 2 on example input."""

    foo = aoc.part2(example1)
    assert foo == 8

def test_score_view():
    arr = np.array([3, 0, 3, 6, 3])
    val = 5
    print(aoc.score_view(arr, val))
@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) is None
