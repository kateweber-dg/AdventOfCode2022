import pathlib
import sys
import numpy as np


def parse(puzzle_input):
    """Parse input."""
    output = [x.split(' ') for x in puzzle_input.split('\n')]
    output = [[x[0], int(x[1])] for x in output]
    return output


class Point(object):
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, direction):
        match direction:
            case 'U':
                self.y += 1
            case 'D':
                self.y -= 1
            case 'L':
                self.x -= 1
            case 'R':
                self.x += 1
            case other:
                print('invalid direction')
                return

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Head(Point):
    def __init__(self):
        super().__init__()

        print(self.__repr__())


class Tail(Point):
    def __init__(self):
        super().__init__()
        self.visited_locations = {(self.x, self.y)}

    def follow(self, head_point):
        # there has to be a generalisable rule here :|
        if head_point.x - self.x + head_point.y - self.y == 3:
            self.move('R')
            self.move('U')
        elif (head_point.x - self.x == 2 and head_point.y - self.y == -1) or \
                (head_point.x - self.x == 1 and head_point.y - self.y == -2):
            self.move('R')
            self.move('D')
        elif (head_point.x - self.x == -2 and head_point.y - self.y == 1) or \
                (head_point.x - self.x == -1 and head_point.y - self.y == 2):
            self.move('L')
            self.move('U')
        elif head_point.x - self.x + head_point.y - self.y == -3:
            self.move('L')
            self.move('D')

        elif head_point.x - self.x > 1:
            self.move('R')
        elif head_point.x - self.x < -1:
            self.move('L')
        elif head_point.y - self.y > 1:
            self.move('U')
        elif head_point.y - self.y < -1:
            self.move('D')

        self.visited_locations.add((self.x, self.y))


def part1(parsed_input):
    """Solve part 1."""
    head = Head()
    tail = Tail()

    for instruction in parsed_input:
        for repeat in range(instruction[1]):
            head.move(instruction[0])
            tail.follow(head)

    return len(tail.visited_locations)

def part2(parsed_input):
    """Solve part 2."""
    pass


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
