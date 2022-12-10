from typing import List
from enum import IntEnum


CYCLE_INDICES = [20, 60, 100, 140, 180, 220]
SPRITE_WIDTH = 3
CRT_HEIGHT, CRT_WIDTH = 40, 6

class CycleCosts(IntEnum):
    NOOP = 1
    ADDX = 2

def read_input(filepath: str) -> List[str]:
    lines: List[str] = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            lines += [line.strip("\n")]

    return lines

def find_signal_strengths(instructions: List[str], at_indices: List[int]) -> List[int]:
    cycle = 1
    register = 1
    registers_of_interest: List[int] = []
    for instr in instructions:
        instr = instr.split(" ")
        if len(instr) == 1:
            if cycle in at_indices:
                registers_of_interest += [register]
            cycle += CycleCosts.NOOP
            continue
        else:
            for _ in range(CycleCosts.ADDX):
                if cycle in at_indices:
                    registers_of_interest += [register]
                cycle += 1

            # Adding op finished, write to register.
            register += int(instr[1])

    if cycle in at_indices:
        registers_of_interest += [register]

    return registers_of_interest

def test_cycle_maths(instructions: List[str]) -> None:
    registers = find_signal_strengths(instructions, list(range(1, 7)))
    assert registers == [1, 1, 1, 4, 4, -1]

def run_test_case() -> None:
    lines = read_input("./small_example.txt")
    test_cycle_maths(lines)

    lines = read_input("./example.txt")
    expected = 13140
    signals = find_signal_strengths(lines, CYCLE_INDICES)
    signal_strengths = [sig * cycle for sig, cycle in zip(signals, CYCLE_INDICES)]
    assert sum(signal_strengths) == expected


if __name__ == "__main__":
    run_test_case()
    lines = read_input("./input.txt")
    signals = find_signal_strengths(lines, CYCLE_INDICES)
    signal_strengths = [sig * cycle for sig, cycle in zip(signals, CYCLE_INDICES)]
    print(sum(signal_strengths))
