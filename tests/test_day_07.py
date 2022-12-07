import pathlib

import pytest

import day_07.day_07 as aoc

PUZZLE_DIR = pathlib.Path(__file__).parent.parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "day_07/example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert len(example1.contents) == 4


def test_directory_size(example1):
    assert example1.contents['a'].contents['e'].get_size() == 584
    assert example1.contents['a'].get_size() == 94853


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 95437


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc.part2(example1) == 24933642


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc.part2(example2) is None
