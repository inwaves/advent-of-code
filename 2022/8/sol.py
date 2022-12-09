import functools
from typing import List

input_filepath = "./input.txt"
TEST_STRING = """30373
25512
65332
33549
35390
"""
EXPECTED = 21


def score_in_one_direction(el: int, direction: List[int]) -> int:
    score = 0
    for other in direction:
        if el <= other:
            score += 1
            break
        if el > other:
            score += 1
    return score


def test_score_in_one_direction():
    input_list = [3, 5, 3]
    assert score_in_one_direction(5, input_list) == 2
    assert score_in_one_direction(3, input_list) == 1
    assert score_in_one_direction(0, input_list) == 1
    input_list = [3]
    assert score_in_one_direction(3, input_list) == 1
    assert score_in_one_direction(3, []) == 0
    assert score_in_one_direction(5, [4, 9]) == 2


def max_scenic_score(lines: List[str]) -> int:
    max_score = 0
    lines = [[int(el) for el in line] for line in lines]
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            column = [lines[i][j] for i in range(0, len(lines))]
            if i == 0 and j == 0:
                print(f"First column looks like {column}")
            el = lines[i][j]
            scores = [
                score_in_one_direction(el, reversed(column[:i])),
                score_in_one_direction(el, column[i + 1 :]),
                score_in_one_direction(el, reversed(lines[i][:j])),
                score_in_one_direction(el, lines[i][j+1:]),
            ]
            #print(f"[{j}][{i}] scores: {scores}")
            scenic_score = functools.reduce(lambda x, y: x * y, scores)
            if scenic_score > max_score:
                #print(f"Max score changed from {max_score} to {scenic_score} by element at [{i}][{j}]")
                #print(f"Row up to: {lines[i][:j]}")
                #print(f"Row past {lines[i][j+1:]}")
                #print(f"Column up to {column[:i]}")
                #print(f"Column past {column[i+1:]}")
                max_score = scenic_score
    return max_score


def tree_visibility(lines: List[str]) -> int:
    """For a tree to be visible, it should either:
    - be on the perimeter
    - be on the interior and be the maximum on its row and column.
    """
    # Trees on perimeter.
    visible_trees = 2 * len(lines[0]) + 2 * (len(lines) - 2)
    print(f"{visible_trees} trees on perimeter.")
    lines = [[int(el) for el in line] for line in lines]
    for i in range(1, len(lines) - 1):
        for j in range(1, len(lines[0]) - 1):
            column = [lines[i][j] for i in range(0, len(lines))]
            # print(
            #    f"Checking element: {lines[i][j]} against its row: {lines[i]} and column: {column}"
            # )
            if (
                max(lines[i][:j]) < lines[i][j]
                or max(lines[i][j + 1 :]) < lines[i][j]
                or max(column[:i]) < lines[i][j]
                or max(column[i + 1 :]) < lines[i][j]
            ):
                # print(f"Largest before, row: {max(lines[i][:j]) < lines[i][j]}, largest after, row: {max(lines[i][j+1:]) < lines[i][j]}")
                # print(f"Largest before, column {max(column[:i]) < lines[i][j]}, largest after, column {max(column[i+1:]) < lines[i][j]}")
                # print(lines[i][:j])
                # print(lines[i][j+1:])
                # print(f"{column=}")
                # print(column[:i])
                # print(column[i+1:])
                print(f"Element {lines[i][j]} passed the test!")

                visible_trees += 1
    return visible_trees


def test_solution():
    assert tree_visibility(TEST_STRING) == EXPECTED


def process_input(input_type: str, input_source: str) -> List[str]:
    lines: List[str] = []
    if input_type == "string":
        for line in input_source.splitlines():
            lines += [line]
    else:
        with open(input_source, "r", encoding="utf-8") as f:
            for line in f:
                lines += [line.strip("\n")]

    return lines


if __name__ == "__main__":
    # Process the input.
    lines = process_input("string", TEST_STRING)
    print(lines)
    test_score_in_one_direction()
    assert max_scenic_score(lines) == 8
    lines = process_input("file", input_filepath)
    print(max_scenic_score(lines))
