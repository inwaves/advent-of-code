from typing import List
from collections import namedtuple
import numpy as np

Point = namedtuple("Point", "x y")


def read_input(filepath: str) -> List[str]:
    lines: List[str] = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            lines += [line.strip("\n")]

    return lines


def run_test_case(expected: int = 1) -> None:
    test_case_movements = read_input("./testcase.txt")
    visits = count_tail_visits(test_case_movements)
    print(f"Got {visits} states visited by test.")
    assert visits == expected


def count_tail_visits(movements: List[str]) -> int:
    board_size = 10000
    board = np.zeros((board_size, board_size))
    knots = [Point(board_size // 2, board_size // 2) for _ in range(10)]
    board[knots[-1]] += 1   # The starting position is counted.

    # Do the movements in order...
    for move_instruction in movements:
        # Play through the move one by one, watching
        # how the tail moves to follow the head.
        move, repeat = move_instruction.split(" ")
        #print(f"Carrying out move: {move_instruction}")
        for _ in range(int(repeat)):
            #print(f"Head moving from {head_position}...")
            knots[0] = move_knot(knots[0], move)
            #print(f"...to {head_position}.")
            knots = propagate_changes(knots)
            board[knots[-1]] += 1
    print(np.nonzero(board))
    return len(np.nonzero(board)[0])

def propagate_changes(knots: List[Point]) -> List[Point]:
    for i in range(1, len(knots)):
        if not knots_adjacent(knots[i-1], knots[i]):
            #print(f"Knot {i} following knot {i-1} from {knots[i]}...")
            knots[i] = move_knot(knots[i], destination=knots[i-1])
            #print(f"...to {knots[i]}.")
    return knots

def move_knot(knot: Point, move: str = None, destination: Point = None) -> Point:
    # When this is specified, it means the tail is
    # trying to follow the head by making a diagonal
    # jump instead of a move in a single dimension.
    if destination:
        if destination.x > knot.x:
            knot = Point(knot.x + 1, knot.y)
        elif destination.x < knot.x:
            knot = Point(knot.x - 1, knot.y)
        if destination.y > knot.y:
            knot = Point(knot.x, knot.y+1)
        elif destination.y < knot.y:
            knot = Point(knot.x, knot.y-1)
        return knot

    # Otherwise just move the head according to the
    # instructions specified...
    if move == "R":
        return Point(knot.x + 1, knot.y)
    elif move == "L":
        return Point(knot.x - 1, knot.y)
    elif move == "U":
        return Point(knot.x, knot.y - 1)
    elif move == "D":
        return Point(knot.x, knot.y + 1)
    return None


def knots_adjacent(head: Point, tail: Point) -> bool:
    return (abs(head.x - tail.x) <= 1) and (abs(head.y - tail.y) <= 1)


def test_knots_adjacent():
    head = Point(5, 5)
    tail = Point(4, 5)
    assert knots_adjacent(head, tail) is True


if __name__ == "__main__":
    run_test_case()
    test_knots_adjacent()
    res = count_tail_visits(read_input("./input.txt"))
    print(f"Output for the actual puzzle: {res}")
