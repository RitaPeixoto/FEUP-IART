from State1 import *
from Utils import *


# Iterative Deepening Depth First Search
def iddfs(state: State1, goal: int = 2, max_depth: int = 15):
    current_max_depth = 1

    while current_max_depth != max_depth:
        root = Node(state)
        stack = [root]
        tree = Graph(root)

        visited = []

        # if the stack is empty we also want to terminate the loop as no more nodes are expandable
        while len(stack) != 0:
            # popping the first node on the stack (current highest depth node)
            node = stack.pop(0)
            # adding the node to the visited list, we do this here so when we are expanding the nodes
            # we dont add to the stack nodes already discovered, including the parent
            visited.append(node.info.final)

            # here we expand said node
            expanded = expand(node.info)

            # if the depth is not already higher than the current max allowed depth
            if node.depth != current_max_depth:
                # for each expanded node we want to add it to the tree, and insert it on the stack so on
                # the next loop we start by the highest depth nodes
                for x in expanded:
                    if x.final not in visited:
                        new_node = Node(x)
                        tree.add_node(new_node)
                        node.add_edge(new_node, 1)
                        stack.insert(0, new_node)

            solution = contains_goal(stack, goal)

            if solution is not None:
                print("Found Solution, Depth", solution.depth)
                return solution, tree

        current_max_depth += 1

    return None, None


