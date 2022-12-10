import pathlib
import sys

import matplotlib.pyplot as plt


def parse(puzzle_input):
    """Parse input."""
    output = [x.split(' ') for x in puzzle_input.split('\n')]
    output = [[x[0], int(x[1])] for x in output]
    return output


class Knot(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.visited_locations = {(self.x, self.y)}

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

    def follow(self, head_point):
        # there has to be a generalisable rule here :|
        dx = head_point.x - self.x
        dy = head_point.y - self.y
        if dx + dy >= 3:
            self.move('R')
            self.move('U')
        elif (dx == 2 and dy == -1) or \
                (dx == 1 and dy == -2):
            self.move('R')
            self.move('D')
        elif (dx == -2 and dy == 1) or \
                (dx == -1 and dy == 2):
            self.move('L')
            self.move('U')
        elif dx + dy <= -3:
            self.move('L')
            self.move('D')

        elif dx > 1:
            self.move('R')
        elif dx < -1:
            self.move('L')
        elif dy > 1:
            self.move('U')
        elif dy < -1:
            self.move('D')

        self.visited_locations.add((self.x, self.y))

    def __repr__(self):
        return f'({self.x}, {self.y})'


def part1(parsed_input):
    """Solve part 1."""
    head = Knot()
    tail = Knot()

    for instruction in parsed_input:
        for repeat in range(instruction[1]):
            head.move(instruction[0])
            tail.follow(head)

    return len(tail.visited_locations)


def plot_grid(rope):
    rope_coords = [[knot.x, knot.y] for knot in rope]
    x_coords = [x[0] for x in rope_coords]
    y_coords = [x[1] for x in rope_coords]
    plt.scatter(x_coords, y_coords)
    for i in range(len(x_coords)):
        plt.annotate(str(i), (x_coords[i], y_coords[i] + 0.2))
    plt.axis('equal')
    plt.show()

def plot_travel(rope):
    travel_coords = rope[-1].visited_locations
    x_coords = [x[0] for x in travel_coords]
    y_coords = [x[1] for x in travel_coords]
    plt.scatter(x_coords, y_coords)
    plt.axis('equal')
    plt.show()


def part2(parsed_input):
    """Solve part 2."""
    n_knots = 10

    rope = [Knot() for x in range(n_knots)]

    for instruction in parsed_input:
        for repeat in range(instruction[1]):
            rope[0].move(instruction[0])
            for i in range(1, n_knots):
                rope[i].follow(rope[i - 1])
    plot_grid(rope)
    plot_travel(rope)
    return len(rope[-1].visited_locations)


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
