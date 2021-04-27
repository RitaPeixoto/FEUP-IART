
from bfs import *
from dfs import *
from ids import *

# Code from this exercise all made by @skdGT

print("---- BFS -----")
node, tree = bfs(State2((3, 3, 1), (3, 3, 1), "Start"))
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
node, tree = dfs(State2((3, 3, 1), (3, 3, 1), "Start"))
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
node, tree = iddfs(State2((3, 3, 1), (3, 3, 1), "Start"))
if node is not None:
    print("- Tree -")
    tree.print_tree()
    path = find_path(node)
    print("- Solution -")
    print_path(path)
else:
    print("- No Solution -")