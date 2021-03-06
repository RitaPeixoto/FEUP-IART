class Edge:
    def __init__(self, origin, destiny, cost):
        self.origin = origin
        self.destiny = destiny
        self.cost = cost
    


class Node:
    def __init__(self, info):
        self.info = info
        self.edges = []
        self.parent = None
        self.depth = 0

    def set_depth(self, depth):
        self.depth = depth
    
    def add_edge(self, destiny, cost):
        self.edges.append(Edge(self, destiny, cost))
        destiny.set_parent(self)
        destiny.set_depth(self.depth + 1)

    def set_parent(self, parent):
        self.parent = parent
    
    def get_children(self):
        children = []
        for edge in self.edges:
            children.append(edge.destiny)
        return children
    
    def get_info(self):
        return str(self.info)


class Graph:

    def __init__(self, root):
        self.root = root
        self.nodes = []

    def print_tree(self):
        print(self.root.get_info())
        self._print_tree(self.root, 1)
    
    def add_node(self, node):
        self.nodes.append(node)
    
    def _print_tree(self, node, level):
        for e in node.edges:
            print(level * "  ", end="")
            print(e.destiny.get_info() + "(" + str(e.cost) +")")
            self._print_tree(e.destiny, level + 1)
