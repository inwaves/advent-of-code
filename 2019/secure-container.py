def hasAscendingOrEqual(number):
    digits = [int(i) for i in str(number)]
    for i in range(len(digits)-1):
        if digits[i+1] < digits[i]:
            return False
    return True

def hasIdenticalAdjacent(number):
    digits = [int(i) for i in str(number)]
    encountered_pair = []
    for i in range(len(digits)-2):
        if digits[i+1] == digits[i] and digits[i+2] != digits[i+1] and digits[i] not in  encountered_pair:
            return True
        if digits[i+1] == digits[i]:
            encountered_pair.append(digits[i])
    if digits[-2]==digits[-1] and digits[-1] not in encountered_pair: return True
    return False

def main():
    start = 372037
    end = 905157
    count = 0
    for i in range(start, end+1):
        if hasAscendingOrEqual(i) and hasIdenticalAdjacent(i):
            count += 1
            # print(i)
    print(count)

if __name__ == "__main__":
    main()