import pathlib

import pytest
import numpy as np
import day_11.day_11 as aoc
from collections import deque

PUZZLE_DIR = pathlib.Path(__file__).parent.parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "day_11/example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)

@pytest.fixture
def example_monkey():
    monkey = aoc.Monkey(name='example')
    monkey.items = deque([78, 98])
    monkey.false_monkey = 3
    monkey.true_monkey = 2
    monkey.test_value = 23
    monkey.operation = ['old', '*', '19']

    return monkey

def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert len(example1) == 4

def test_monkey(example_monkey):

    assert example_monkey.operation_mapper('+')(3, 2) == 5
    assert example_monkey.operation_mapper('*')(3, 2) == 6
    assert example_monkey.operate(2) == 38
    example_monkey.operation = ['old', '*', 'old']
    assert example_monkey.operate(3) == 9
    assert example_monkey.test_worry(32) == False
    assert example_monkey.test_worry(46) == True
    print('wait_here')


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc.part1(example1) == 10605

def test_part2_example1(example1):
    """Test part 2 on example input."""
    pass

def test_part2_example2(example2):
    """Test part 2 on example input."""
    pass



