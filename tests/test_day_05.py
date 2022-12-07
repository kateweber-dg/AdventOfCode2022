import pathlib
import pytest
from day_05 import day_05 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent.parent

@pytest.fixture
def example1():
    print(PUZZLE_DIR)
    puzzle_input = (PUZZLE_DIR / "day_05/example1.txt").read_text()
    return aoc.parse(puzzle_input)

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1['stack'] == {1: ['Z', 'N'], 2: ['M', 'C', 'D'], 3: ['P']}
    assert example1['instructions'] == [[1, 2, 1], [3, 1, 3], [2, 2, 1], [1, 1, 2]]

def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 'CMZ'


def test_part2_example1(example1):
    """Test part 2 on example input."""
    foo = aoc.part2(example1)
    assert foo == 'MCD'

@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) == ...