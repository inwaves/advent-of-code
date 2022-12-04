filepath = "./input.txt"

max = 0
totals = []
with open(filepath, "r") as f:
    # While not finished, read line from file.
    current_total = 0
    for line in f:
        if line != "\n":
            current_total += int(line)
        else:
            totals.append(current_total)
            current_total = 0
totals.sort(reverse=True)
print(sum(totals[:3]))
