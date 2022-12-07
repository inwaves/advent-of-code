from typing import Tuple, List


def sort_crates() -> None:
    filepath = "./input.txt"
    stack_data = []  # Stacks as list of lists.

    with open(filepath, "r") as f:
        # Start by parsing the stack data.
        line = ""
        while line != "\n":
            line = next(f)
            stack_data += [line]

        stacks = parse_stacks(stack_data[:-2], stack_data[-2][-2])
        print(stacks)
        # Then, read each move and apply it to the stacks.
        for line in f:
            crates_moved, src_stack, dest_stack = parse_move(line)
            stacks[dest_stack - 1] += stacks[src_stack - 1][-crates_moved:]
            stacks[src_stack - 1] = stacks[src_stack - 1][:-crates_moved]
    readout = "".join([stack.pop() for stack in stacks])
    print(readout)


def parse_stacks(stack_data: List[str], num_stacks: int) -> List[List[str]]:
    """Take in the lines that specify the initial state of the stacks.
    Return the stacks parsed as lists containing strings (crate names)."""
    ns = int(num_stacks)
    stack_data = [s.strip("\n").ljust(ns * 4 - 1) for s in stack_data]
    split_lines = [s[1::4] for s in stack_data]
    print(split_lines)
    stacks = [[] for _ in range(ns)]

    for line in split_lines:
        # The "gap" between stacks in the text is 4 chars; the actual crate name starts at index 1.
        # For example, "[R]    [G]" ends up with a string such as "R G..."
        # where gaps at index i means no item to add to stack i.
        crates = list(line)
        for i, crate in enumerate(crates):
            if crate != " ":
                stacks[i] += [crate]

    # We parse top to bottom, so we should reverse.
    # (Or you could just pop from the front of the list.)
    return [list(reversed(stack)) for stack in stacks]


def parse_move(line: str) -> Tuple[int, int, int]:
    """Parse one move line and return a tuple of:
    num_crates_moved, source_stack, destination_stack."""
    words = line.split(" ")
    return (int(words[1]), int(words[3]), int(words[-1]))


def test_parse_stacks():
    stack_data = []
    with open("./input.txt", "r") as f:
        line = ""
        while line != "\n":
            line = next(f)
            stack_data += [line]
    stacks = parse_stacks(stack_data[:-2], stack_data[-2][-2])
    print(stacks)


def test_parse_move():
    lines = ["move 3 from 8 to 9", "move 15 from 4 to 1"]
    expected = [(3, 8, 9), (15, 4, 1)]
    for line, parsed in zip(lines, expected):
        assert parse_move(line) == parsed


if __name__ == "__main__":
    test_parse_move()
    test_parse_stacks()
    sort_crates()
