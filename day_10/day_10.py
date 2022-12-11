import pathlib
import sys
import numpy as np

def parse(puzzle_input):
    """Parse input."""
    splits = [x.split(' ') for x in puzzle_input.split('\n')]
    output = []

    for row in splits:
        if len(row) > 1:
            row[1] = int(row[1])
        output.append(row)
    return output


class Register(object):
    def __init__(self):
        self.cycle = 0
        self.value = 1
        self.history = [{'cycle': self.cycle,
                         'value': self.value,
                         'instruction_row': 0,
                         'instructions': None}]
        self.waiting_instruction = []

    def noop(self, instruction_row_index):
        if len(self.waiting_instruction) > 0:
            self.value += self.waiting_instruction.pop()
        self.tick(instruction_row_index, ['noop', None])
        self.waiting_instruction = []

    def addx(self, instruction_row_index, instructions):
        if len(self.waiting_instruction) >0:
            self.value += self.waiting_instruction.pop()
        self.tick(instruction_row_index, instructions)
        self.tick(instruction_row_index, instructions)
        self.waiting_instruction.append(instructions[1])

    def tick(self, instruction_row_index, instructions):
        self.cycle += 1
        self.history.append({'cycle': self.cycle,
                             'value': self.value,
                             'instruction_row': instruction_row_index,
                             'instructions': instructions})

    def __repr__(self):
        return self.value


def part1(parsed_input):
    """Solve part 1."""
    register = fill_register(parsed_input)

    signal_strengths = 0
    for sample in range(20, len(register.history), 40):
        entry = [x for x in register.history if x['cycle'] == sample][0]
        print(sample, entry['value'], sample * entry['value'])
        signal_strengths += sample * entry['value']

    return signal_strengths


def fill_register(parsed_input):
    register = Register()
    for index, row in enumerate(parsed_input):
        if row[0] == 'noop':
            register.noop(index)
        else:
            register.addx(index, row)
    register.noop(index + 1)
    return register

def wrap_crt(crt):
    for row in crt:
        print (''.join(row))

def point_in_sprite(point, sprite_position):
    if point in range(sprite_position - 1, sprite_position+2):
        return True
    else:
        return False

def part2(parsed_input):
    """Solve part 2."""
    completed_history = fill_register(parsed_input).history
    crt = np.full((6, 40), ' ', dtype='str')

    for crt_position, cycle_information in enumerate(completed_history[1:-1]):
        sprite_position = cycle_information['value']
        horiz_index = crt_position % 40
        horiz_row = crt_position // 40
        if point_in_sprite(horiz_index, sprite_position):
            crt[horiz_row, horiz_index] = '#'
        else:
            crt[horiz_row, horiz_index] = '.'
        # print(''.join(crt[horiz_row]))


    return wrap_crt(crt)



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
