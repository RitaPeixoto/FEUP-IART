from Graph import *
import copy


# we only need to no if we are doing a_star or greedy when calculating the cost
def expand(state:Node, a_star: bool=False):
    expansion = []

    matrix, pos = state.matrix, state.empty_pos
    size = len(matrix)
    n_cols = len(matrix[0])
    row = pos // size
    col = pos % size

    
    if(row != 0): #Move up
        aux_matrix = copy.deepcopy(matrix)
        zero, numb = matrix[row][col], matrix[row-1][col]
        aux_matrix[row][col], aux_matrix[row-1][col] = numb,zero
        expansion.append(Node(aux_matrix, (row - 1) * size + col, manhattan(aux_matrix), state.dist + 1)) if a_star else expansion.append(Node(aux_matrix, (row - 1) * size + col, manhattan(aux_matrix), 0))
   
    if(row != (size-1)):  # Move Down
        aux_matrix = copy.deepcopy(matrix)
        zero,numb=matrix[row][col],matrix[row+1][col]
        aux_matrix[row][col],aux_matrix[row+1][col]=numb,zero
        expansion.append(Node(aux_matrix,(row+1)*size+col,manhattan(aux_matrix),state.dist+1)) if a_star else expansion.append(Node(aux_matrix,(row+1)*size+col,manhattan(aux_matrix),0))
    
    if(col != 0): # Move Left
        aux_matrix = copy.deepcopy(matrix)
        zero, numb = matrix[row][col], matrix[row][col - 1]
        aux_matrix[row][col], aux_matrix[row][col - 1] = numb, zero
        expansion.append(Node(aux_matrix, row * size + (col - 1), manhattan(aux_matrix), state.dist + 1)) if a_star else expansion.append(Node(aux_matrix, row * size + (col - 1), manhattan(aux_matrix), 0))
   
    if(col != (n_cols - 1)):  # Move Right
        aux_matrix = copy.deepcopy(matrix)
        zero,numb=matrix[row][col], matrix[row][col + 1]
        aux_matrix[row][col], aux_matrix[row][col + 1] = numb, zero
        expansion.append(Node(aux_matrix, row * size + (col + 1),manhattan(aux_matrix),state.dist + 1)) if a_star else expansion.append(Node(aux_matrix, row * size + (col + 1), manhattan(aux_matrix), 0))

    for children in expansion:
        children.parent = state

    return expansion


def found_goal(states, goal: list):
    for state in states:
        if state.matrix == goal:
            return True
    return False

def calculate_z_pos(matrix: list):
    pos = 0
    found = False
    for row in matrix:
        for col in row:
            if col == 0:
                found = True
                break
            pos += 1
        if found:
            break
    
    return pos

def manhattan(matrix: list):
    size = len(matrix)
    n_cols = len(matrix[0])
    row = 0
    col = 0
    distance = 0
    for line in matrix:
        for number in line:
            if number == 0:
                col += 1
                continue
            new_pos = number - 1
            new_row = new_pos//size
            new_col = new_pos%n_cols
            distance += abs(new_row - row) + abs(new_col - col)
            col += 1
        row += 1
    return distance


def bfs(state: Node, max_depth: int = 100, goal: list=[[1,2,3],[4,5,6],[7,8,0]]):
    states = [state]

    graph = Graph()
    graph.new_depth()
    graph.add_node(state, 1)
    for depth in range(1, max_depth + 1):
        expanded_states = []
        for s in states:
            if s in graph.visited:
                continue
            aux = expand(s)
            for e in aux:
                expanded_states.append(e)
            graph.visit(s)
        states = expanded_states
        graph.new_depth()
        [graph.add_node(x, depth + 1) for x in states]
        if found_goal(states, goal):
            print("Found Goal. Depth:", depth + 1)
            return graph, depth + 1

def check_solvability(matrix: list):
    flat_list = [item for sublist in matrix for item in sublist]
    inversions = 0

    for x in range(0, len(flat_list)):
        for y in range(x + 1, len(flat_list)):
            inversions += 1 if(flat_list[x] > flat_list[y] and flat_list[y] != 0) else 0
    return inversions % 2 == 0 




if __name__ == "__main__":
    print("---- BFS -----")
    print("8-PUZZLE")
    puzzle1 = [[5,2,8],[4,1,7],[0,3,6]]
    puzzle2 = [[1,2,3],[4,5,6],[7,0,8]]
    puzzle3 = [[0,2,3],[1,5,6],[4,7,8]]
    puzzle4 = [[5,1,3,4],[2,0,7,8],[10,6,11,12],[9,13,14,15]]

    pos = calculate_z_pos(puzzle1)

    if(check_solvability(puzzle1)):
        print("- Solution -")
    else: 
        print("- No Solution -")

    graph, depth = bfs(Node(puzzle1, pos))

    print(graph.expanded_states())
