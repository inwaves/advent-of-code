from typing import List
import os

def read_input(day: str) -> List[str]:
    filename = os.path.join(os.getcwd(), "2020/inputs/" + day + "_input.txt")
    with open(filename, 'r') as f:
        rows = f.readlines()
        
    return rows

def process_input(rows: List[str]) -> List:
    
    # can't operate on the same list so let's create
    # a list of tuples
    processed_rows = []
    for row in rows:
        tokens = row.split()
        min_freq, max_freq = tokens[0].split("-")
        letter = tokens[1][0]
        password = tokens[2]
        processed_rows.append((min_freq, max_freq, letter, password))
        
    return processed_rows