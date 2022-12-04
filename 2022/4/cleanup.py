filepath = "./input.txt"
counter = 0

with open(filepath, "r") as f:
    for line in f:
        # TODO: check that input format is correct.
        first_elf, second_elf = line.split(",")
        (first_start, first_end) = first_elf.split("-")
        (second_start, second_end) = second_elf.split("-")
        first_range = set(list(range(int(first_start), int(first_end)+1)))
        second_range = set(list(range(int(second_start), int(second_end)+1)))
        if len(first_range & second_range) > 0:
            counter += 1

print(counter)
