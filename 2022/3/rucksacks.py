input_filepath = "./input.txt"

lowercase_values = {chr(i): j for (i, j) in zip(range(ord("a"), ord("z")+1), range(1, 27))}
uppercase_values = {chr(i): j for (i, j) in zip(range(ord("A"), ord("Z")+1), range(27, 53))}
values = {**lowercase_values, **uppercase_values, "\n": 0}
total = 0
with open(input_filepath, "r") as f:
    buf = []
    for line in f:
        line = line.strip("\n")
        if len(buf) < 3:
            buf.append(line)
        else:
            print(f"{buf=}")
            sets = [set(line) for line in buf]
            badge = sets[0] & sets[1] & sets[2]
            print(f"{badge=}")
            total += values[badge.pop()]
            buf = [line]
    sets = [set(line) for line in buf]
    badge = sets[0] & sets[1] & sets[2]
    print(f"{badge=}")
    total += values[badge.pop()]
print(total)
