from utils import read_input
from typing import List


def toboggan_one(forest: List[str]) -> int:
    TREE = "#"
    ACROSS, DOWN = 3, 1
    current_pos, trees = [0, 0], 0
    
    # store the input as a list of lists: 323x31
    forest_contents = [list(elem[:-1]) for elem in forest]
    print(len(forest_contents))
    row_length = len(forest_contents[0])
    # go across 3, down 1 until you reach the bottom
    # what is the bottom? the last row in the input
    while current_pos[1] + DOWN < len(forest_contents):
        print("curpos: {}, trees: {}".format(current_pos, trees))
        if forest_contents[current_pos[1]][current_pos[0]] == TREE:
            trees += 1

        current_pos[0] = (current_pos[0]+ACROSS) % row_length
        current_pos[1] += DOWN
    return trees


def toboggan_two(forest: List[str]) -> int:
    return -1


if __name__ == "__main__":
    forest = read_input("day3")
    print("The answer to part 1: {}".format(toboggan_one(forest)))
    print("The answer to part 2: {}".format(toboggan_two(forest)))
