from typing import List
from enum import IntEnum


CYCLE_INDICES = [20, 60, 100, 140, 180, 220]
SPRITE_WIDTH = 3
CRT_WIDTH, CRT_HEIGHT = 40, 6

expected_screen = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""

class CycleCosts(IntEnum):
    NOOP = 1
    ADDX = 2

def read_input(filepath: str) -> List[str]:
    lines: List[str] = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            lines += [line.strip("\n")]

    return lines

def run_test_case() -> None:
    lines = read_input("./example.txt")
    output = draw_crt(lines)
    assert output == expected_screen

def draw_pixel(cycle: int, register: int, line: str, crt_lines: List[str]) -> str:
    new_char ="#" if abs(((cycle-1) % CRT_WIDTH)-register) <= 1 else "."
    line += new_char
    if not cycle % CRT_WIDTH:
        crt_lines += [line]
        line = ""
    return line, crt_lines


def draw_crt(instructions: List[str]) -> str:
    cycle = 1
    register = 1
    crt_lines: List[str] = []
    line = ""
    for instr in instructions:
        instr = instr.split(" ")
        if len(instr) == 1:
            line, crt_lines = draw_pixel(cycle, register, line, crt_lines)
            cycle += CycleCosts.NOOP
        else:
            for _ in range(CycleCosts.ADDX):
                line, crt_lines = draw_pixel(cycle, register, line, crt_lines)
                cycle += 1

            # Adding op finished, write to register.
            register += int(instr[1])

    return "\n".join(crt_lines)

if __name__ == "__main__":
    #run_test_case()
    lines = read_input("./input.txt")
    output = draw_crt(lines)
    print(output)
