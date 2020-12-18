import os

def trace_one(instr, wire_path, curpos):
    if instr.startswith("R"):  # trace right
        for x in range(curpos[0], curpos[0]+int(instr[1:])+1):
            wire_path[x][curpos[1]] = 1
        return [curpos[0]+int(instr[1:])+1, curpos[1]]
    elif instr.startswith("L"): # trace left
        for x in range(curpos[0]-int(instr[1:])-1, curpos[0]):
            wire_path[x][curpos[1]] = 1
        return [curpos[0]-int(instr[1:])-1, curpos[1]]
    elif instr.startswith("U"): # trace up
        for y in range(curpos[1], curpos[1]+int(instr[1:])+1):
            wire_path[curpos[0]][y] = 1
        return [curpos[0], curpos[1]+int(instr[1:])+1]
    elif instr.startswith("D"): # trace down
        for y in range(curpos[1]-int(instr[1:])-1, curpos[1]):
            wire_path[curpos[0]][y] = 1
        return [curpos[0], curpos[1]-int(instr[1:])-1]
    else:
        raise ValueError("Instruction unclear.")
        

def trace_wire(path_instructions, wire_path):
    curpos = [5000, 5000]
    for instr in path_instructions:
        curpos = trace_one(instr, wire_path, curpos)

def main():
    with open("wires.txt") as f:
        content = f.readlines()
    fw_instructions = content[0].rstrip('\n').split(',')
    sw_instructions = content[1].rstrip('\n').split(',')

    fw_path = [[0 for x in range(10000)] for y in range(10000)]
    sw_path = [[0 for x in range(10000)] for y in range(10000)]

    trace_wire(fw_instructions, fw_path)
    print("Traced first wire.")
    print(fw_path)
    # trace_wire(sw_instructions, sw_path)
    # print("Traced second wire.")

if __name__ == "__main__":
    os.chdir(os.getcwd() + "/advent-of-code/")
    main()