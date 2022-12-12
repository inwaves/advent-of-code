from typing import List, Callable, Tuple
from functools import total_ordering
import sys

def read_input(filepath: str) -> List[str]:
    lines: List[str] = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            lines += [line.strip("\n")]

    return lines

def run_test_case() -> None:
    lines = read_input("./example.txt")
    expected = 2713310158
    monkeys = parse_monkeys(lines)
    print(monkeys)
    for _ in range(10000):
        play_round(monkeys)
    output = [monkey.inspections_made for monkey in sorted(monkeys)]
    print(output)
    assert output[-1] * output[-2] == expected

@total_ordering
class Monkey:
    def __init__(self, order: int, inventory: List[int]) -> None:
        self.order: int = order
        self.inventory: List[int] = inventory
        self.predicate: Callable[[int], bool] = None
        self.inspection: Callable[[int], int] = None
        self.destinations: Tuple[int, int] = None
        self.inspections_made: int = 0

    def setup_inspection(self, operation: str) -> None:
        self.inspection = lambda old : eval(operation)

    def setup_predicate(self, divisible_by: int) -> None:
        print(f"Predicate for monkey {self.order}: divisible by {divisible_by}")
        self.div_by = divisible_by
        self.predicate = lambda x : (x % divisible_by) == 0

    def inspect(self) -> None:
        it = self.inventory[0]
        self.inventory[0] = sys.maxsize - self.inspection(self.inventory[0])
        self.inspections_made += 1
        print(f"Inspection from Monkey {self.order} on item {it} turns it to {self.inventory[0]}")

    def eval_and_throw_item(self) -> Tuple[int, int]:
        item = self.inventory[0]
        destination = self.destinations[self.predicate(item)]
        self.inventory = self.inventory[1:]
        print(f"Monkey {self.order} throwing item {item} to monkey {destination}")
        return destination, item

    def receive_item(self, item: int) -> None:
        print(f"Monkey {self.order} received item {item}.")
        self.inventory += [item]

    def __eq__(self, other: "Monkey") -> bool:
        return self.inspections_made == other.inspections_made

    def __lt__(self, other: "Monkey") -> bool:
        return self.inspections_made < other.inspections_made

    def __repr__(self) -> str:
        return f"""Monkey {self.order} has items: {self.inventory}.
        It checks divisibility by {self.predicate} and applies {self.inspection}. If true, throws to {self.destinations[True]}, else {self.destinations[False]}\n\n"""

def parse_monkeys(lines: List[str]) -> List[Monkey]:
    monkeys: List[Monkey] = []
    for line in lines:
        if "Monkey " in line:
            continue
        elif "Starting items:" in line:
            item_list = (line.split(":")[1]).split(",")
            item_list = [int(item) for item in item_list]
            monkey = Monkey(len(monkeys), item_list)
            monkeys += [monkey]
        elif "Operation: " in line:
            operation = line.split("=")[1].strip(" ")
            print(f"Monkey {monkey.order} has operation {operation}.")
            monkey.setup_inspection(operation)
        elif line != "":
            int_of_interest = int(line.split(" ")[-1])
            if "Test: " in line:
                monkey.setup_predicate(int_of_interest)
            elif "If true: " in line:
                monkey.destinations = (0, int_of_interest)
            elif "If false: " in line:
                monkey.destinations = (int_of_interest, monkey.destinations[1])
    return monkeys

def play_round(monkeys: List[Monkey]) -> None:
    for monkey in monkeys:
        while len(monkey.inventory) > 0:
            print(f"Monkey {monkey.order} doing an operation...")
            monkey.inspect()
            dest_idx, item = monkey.eval_and_throw_item()
            monkeys[dest_idx].receive_item(item)

def test_monkeys(monkeys: List[Monkey]) -> None:
    print(monkeys[1])
    print(f"Inspecting one item: {monkeys[1].inventory[0]}...")
    monkeys[1].inspect(0)
    print(f"Monkey 1 takes 30 to {monkeys[1].inspection(30)}")
    print(f"It also checks divisibility: {monkeys[1].predicate(30)}")
    print(monkeys[1])

if __name__ == "__main__":
    run_test_case()
    lines = read_input("./input.txt")
    monkeys = parse_monkeys(lines)
    print(monkeys)
    #test_monkeys(monkeys)
    for _ in range(20):
        play_round(monkeys)
    print([monkey.inspections_made for monkey in sorted(monkeys)])
