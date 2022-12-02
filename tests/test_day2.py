import pathlib
import pytest
from day2 import day2 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent.parent

@pytest.fixture
def example1():
    print(PUZZLE_DIR)
    puzzle_input = (PUZZLE_DIR / "day2/example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "day2/example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [["A", "Y"], ["B", "X"], ["C", "Z"]]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 15


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 12

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...