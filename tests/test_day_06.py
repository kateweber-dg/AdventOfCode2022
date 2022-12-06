import pathlib
import pytest
import day_06.day_06 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent.parent

@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "day_06/example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert isinstance(example1, list)

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == [7, 5, 6, 10, 11]

def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == [19, 23, 23, 29, 26]

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...