from typing import List

MAX_SIZE = 100_000
TOTAL_DISK_SIZE = 70_000_000
SIZE_NEEDED = 30_000_000

class TreeNode:
    def __init__(self, name: str, size: int = 0, parent: "TreeNode" = None) -> None:
        self.name = name
        self.size = size
        self.children = {}
        self.parent = parent

    def add_child(self, child_name: str, size: int) -> None:
        child = TreeNode(child_name, size, self)
        self.children[child_name] = child

    def get_size(self, minsize_found: int, minsize_required: int) -> int:
        """Go through this node's children recursively to get their size.
        This node's size is the sum of all direct and indirect files' sizes contained in it. If the node itself has a size, add it. (If not it'll be zero.)
        """
        children_size = 0
        for child in self.children:
            child_size, minsize_found = self.children[child].get_size(minsize_found, minsize_required)
            children_size += child_size

        if children_size >= minsize_required and children_size < minsize_found:
            minsize_found = children_size

        total_node_size = self.size + children_size
        return total_node_size, minsize_found


def parse_lines(lines: List[str]) -> TreeNode:
    """Parse a list of lines into a tree structure.
    Information I know:
        - lines that start with $ are commands;
        - lines that start with dir specify a directory;
        - lines that start with a number specify a file size;

    What else?
        - to parse the tree correctly I need to follow where I am, possibly building and traversing the TreeNode as I go.
            - so e.g. $ cd .. means 'node.parent', cd dir_name means 'node.child' and so on.
    """
    assert len(lines) == 1105
    root = TreeNode("/", 0) # TODO: how do I keep a copy of root as it's being modified?

    current_node = root
    index = 1
    while index < len(lines):
        # There are two commands: cd [arg] and ls.
        # When I see cd [arg], move into root.children["arg"].
        if "$ cd" in lines[index]:
            arg = lines[index][5:]
            if ".." in arg:
                current_node = current_node.parent
            else:
                current_node = current_node.children[arg]
            index += 1  # Advance to next line.

        # When I see ls, process all lines until the next $, and add child nodes.
        # Results of ls are lines[index:ls_result_index]
        if "$ ls" in lines[index]:
            ls_result_index = index + 1
            while ls_result_index < len(lines) and "$ " not in lines[ls_result_index]:
                # Parse the line.
                result = lines[ls_result_index].split(" ")
                if result[0] == "dir":
                    current_node.add_child(result[1], 0)
                else:
                    current_node.add_child(result[1], int(result[0]))
                ls_result_index += 1
            index = ls_result_index

    return root

if __name__ == "__main__":
    input_filepath = "./input.txt"
    cmds = []

    with open(input_filepath, "r", encoding="utf-8") as f:
        for line in f:
            cmds += [line]

    root = parse_lines(cmds)
    root_size, accumulated = root.get_size(0, 0)
    smallest_size_needed = SIZE_NEEDED - (TOTAL_DISK_SIZE - root_size)
    print(f"{root_size=}, {smallest_size_needed}")
    root_size, minsize_found = root.get_size(1e10, smallest_size_needed)
    print(root_size, minsize_found)
