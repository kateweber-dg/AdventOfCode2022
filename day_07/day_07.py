import pathlib
import re
import sys


class File(object):
    def __init__(self, name, file_size):
        self.name = name
        self.file_size = file_size
        self.size = 0


    def __repr__(self):
        return f'{self.name} (file, size={self.file_size})'


class Directory(object):
    def __init__(self, name: str):
        self.name = name
        self.contents = {}
        self.parent_dir = None
        self.size_array = []

    def add_item(self, item):
        if isinstance(item, Directory):
            item.parent_dir = self
        self.contents[item.name] = item

    def get_size(self):
        size = 0
        for key, item in self.contents.items():
            if isinstance(item, File):
                size += item.file_size
            else:
                size += item.get_size()
        return size

    def walk_sizes(self, size_array = []):
        if size_array == []:
            size_array = [self.get_size()]
        for key, item in self.contents.items():
            if isinstance(item, Directory):
                size_array.append(item.get_size())
                item.walk_sizes(size_array)
        return size_array

    def __repr__(self):
        return f"""dir: {self.name}: Parent = {self.parent_dir}"""


def parse(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split('\n')

    root = Directory('root')
    current_dir = root
    line_number = 0
    for line in lines:
        line_number += 1
        if line[0:4] == '$ cd':
            cd_dir_str = line.split(' ')[-1]
            if cd_dir_str == '/':
                continue
            if cd_dir_str == '..':
                current_dir = current_dir.parent_dir
                continue
            else:
                current_dir = current_dir.contents[cd_dir_str]
                continue
        if line[0:4] == '$ ls':
            continue
        else:
            item = line.split(' ')
            if item[0] == 'dir':
                dir_name = item[1]
                new_dir = Directory(name=dir_name)
                current_dir.add_item(new_dir)
                new_dir.parent_dir = current_dir
            else:
                current_dir.add_item(File(name=item[1], file_size=int(item[0])))
    return root


def part1(parsed_input):
    """Solve part 1."""

    root = parsed_input
    size_array = root.walk_sizes()
    return sum([x for x in size_array if x <= 100000])


def part2(parsed_input):
    """Solve part 2."""
    total_disk_space = 70000000
    needed_space = 30000000
    root = parsed_input
    size_array = root.walk_sizes()

    unused_space = 70000000 - size_array[0]
    required_to_delete = needed_space - unused_space

    return min([x for x in size_array if x > required_to_delete])


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
