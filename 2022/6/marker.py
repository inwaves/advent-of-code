from typing import Any, List

filepath = "./input.txt"


def marker_string_manip(filepath: str, window_size: int) -> int:
    with open(filepath, "r", encoding="utf-8") as f:
        input_string = next(f)

    if len(set(input_string[:window_size])) == window_size:
        return 0
    else:
        for i in range(window_size, len(input_string)):
            if len(set(input_string[i - window_size : i])) == window_size:
                return i
    return -1


def marker_generator(filepath: str, window_size: int) -> int:
    """This uses less memory, since it never stores the entire string."""

    def generate_file():
        with open(filepath, "r", encoding="utf-8") as f:
            yield from f.read()

    gen = generate_file()
    ctr = 0
    sliding_window = []
    while c := next(gen):
        ctr += 1
        if len(sliding_window) < window_size:
            sliding_window += [c]
        else:
            sliding_window = sliding_window[1:] + [c]
        if len(set(sliding_window)) == window_size:
            return ctr
    return -1


def dedup_list(li: List[Any]) -> List[Any]:
    """This is O(n) time (one loop through list) and O(n) space (copy of list + dict)."""
    kvs = {} # Can I do it without a dict?
    deduped = [] # Can I do it in-place?
    for item in li:
        if item not in kvs:
            deduped += [item]
            kvs[item] = 0
    return deduped


if __name__ == "__main__":
    print(f"{marker_string_manip(filepath, 4)}")
    print(f"{marker_generator(filepath, 4)}")

    print(f"{dedup_list([1, 1, 3, 4, 3, 9])}")
