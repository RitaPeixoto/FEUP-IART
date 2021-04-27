class State2:
    def __init__(self, initial, final, info, cost=1):
        self.initial = initial
        self.final = final
        self.info = info
        self.cost = cost

    def __str__(self):
        return str(self.initial) + " - " + self.info + " - " + str(self.final) + " :: Cost - " + str(self.cost)


def filter_state(State2):
    m, c, b = State2.final
    if m > 3 or m < 0 or c > 3 or c < 0 or m > 3 or m < 0 or c > 3 or c < 0:
        return False

    if m < c != 0:
        return False
    if (m - 3) < (c - 3) != 0:
        return False
    if m >= c and (m - 3) >= (c - 3):
        return True
    else:
        return False


def expand(operation: State2):
    m, c, b = operation.final

    expanded = []

    if b == 1:
        expanded.append(State2(operation.final, (m, c - 1, -b), "1C Start -> End"))
        expanded.append(State2(operation.final, (m - 1, c, -b), "1M Start -> End"))
        expanded.append(State2(operation.final, (m - 2, c, -b), "2M Start -> End"))
        expanded.append(State2(operation.final, (m, c - 2, -b), "2C Start -> End"))
        expanded.append(State2(operation.final, (m - 1, c - 1, -b), "1C1M Start -> End"))
    else:
        expanded.append(State2(operation.final, (m, c + 1, -b), "1C End -> Start"))
        expanded.append(State2(operation.final, (m + 1, c, -b), "1M End -> Start"))
        expanded.append(State2(operation.final, (m + 2, c, -b), "2M End -> Start"))
        expanded.append(State2(operation.final, (m, c + 2, -b), "2C End -> Start"))
        expanded.append(State2(operation.final, (m + 1, c + 1, -b), "1C1M End -> Start"))

    expanded = filter(filter_state, expanded)

    return expanded