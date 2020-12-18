def fixcodes(content):
    x = 0
    while content[x] != 99:
        if content[x] == 1:
            content[content[x+3]] = content[content[x+1]] + content[content[x+2]]
        elif content[x] == 2:
            content[content[x+3]] = content[content[x+1]] * content[content[x+2]]
        else:
            print("Invalid opcode at: " + str(x) + ", value unrecognised: " + str(content[x]))
            break
        x += 4
    if content[0] == 19690720:
        print(100*content[1]+content[2])
        return 0

def main():       
    with open('opcode.txt') as f:
        content = f.readline()

    clist = content.split(',')
    clist  = [int(x) for x in clist] # parsing the string

    for i in range(100):
        for j in range(100):
            clist2 = clist[:]
            clist2[1] = i
            clist2[2] = j
            if fixcodes(clist2) == 0:
                break
    

if __name__ == "__main__":
    main()

