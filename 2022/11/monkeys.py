from typing import List, Callable

def read_input(filepath: str) -> List[str]:
    lines: List[str] = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            lines += [line.strip("\n")]

    return lines

def run_test_case() -> None:
    lines = read_input("./example.txt")
    assert output == expected


class Monkey:
    def __init__(self, order: int, inventory: List[int]) -> None:
        self.order = order
        self.inventory = inventory

    def inspect(self, item: int) -> None:
        pass

    def test(self, item: int) -> bool:
        pass

    def throw(self, predicate: bool) -> None:
        pass

def divisible_by(n: int, k: int) -> bool:
    return not n % k

if __name__ == "__main__":
    #run_test_case()
    lines = read_input("./input.txt")
    monkeys: List[Monkey] = []
    monkeys_items: List[List[int]] = []
    monkeys_operations: List[List[Callable[int, int]]] = []
    monkeys_predicates: List[List[Callable[[int, int], bool]]] = []
    for line in lines:
        if "Starting items:" in line:
            item_list = (line.split(":")[1]).split(",")
            item_list = [int(item) for item in item_list]
            monkey = Monkey(len(monkeys), item_list)
        elif "Operation: " in line:
            parse_operation()
            monkey.inspect = operation
        elif "Test: " in line:
            parse_test()
            monkey.test = test
        elif "If true: " in line:
            true_throw = parse_true()
            monkey.true_throw = true_throw
        elif "If false: " in line:
            false_throw = parse_false()
            monkey.false_throw = false_throw

    print(monkeys_items)
