from bfs import *
from dfs import *
from ids import *

# Code from this exercise all made by @skdGT

print("---- BFS -----")
node, tree = bfs(State1((0, 0), (0, 0), "Start"), goal=2)
print("- Tree -")
tree.print_tree()
if node is not None:
    path = find_path(node)
    print("- Solution -")
    print_path(path)
else:
    print("- No Solution -")
print('\n\n\n\n\n\n')

print("---- DFS -----")
node, tree = dfs(State1((0, 0), (0, 0), "Start"), max_depth = 10)  
print("- Tree -")
tree.print_tree()
if node is not None:
    path = find_path(node)
    print("- Solution -")
    print_path(path)
else:
    print("- No Solution -")

print('\n\n\n\n\n\n')
print("---- IDDFS -----")
node, tree = iddfs(State1((0, 0), (0, 0), "Start"))
if node is not None:
    print("- Tree -")
    tree.print_tree()
    path = find_path(node)
    print("- Solution -")
    print_path(path)
else:
    print("- No Solution -")