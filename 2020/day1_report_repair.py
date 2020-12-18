import os
from typing import List
from utils import read_input

def rr_partone(input_rows: List[int]) -> int:
    for elem in input_rows:
        if 2020-elem in input_rows:
            return elem*(2020-elem)
    return -1

def rr_parttwo(input_rows: List[int]) -> int:
    for el1 in input_rows:
        for el2 in input_rows:
            if 2020-(el1+el2) in input_rows:
                return el1*el2*(2020-el1-el2)
    return -1

def report_repair() -> None:
    input_rows = read_input(os.path.join(os.getcwd(), "2020/inputs/day1_input.txt"))
    input_rows = [int(elem) for elem in input_rows]
    
    print("Answer to part 1: {}".format(rr_partone(input_rows)))
    print("Answer to part 2: {}".format(rr_parttwo(input_rows)))
    
    
    
if __name__ == "__main__":
    print(report_repair())