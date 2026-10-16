from collections import deque

def bfs(problem):
    root = problem.root()
    created = 1                                  # the root counts as created
    frontier = deque([root])
    while frontier:
        node = frontier.popleft()
        if problem.is_goal(node.state):          # goal test when node is expanded
            return node.state, created, node.path()
        for child in problem.expand(node):
            if node.on_path(child.state):        # skip cycles
                continue
            created += 1
            frontier.append(child)
    return None, created, []


def dfs(problem):
    root = problem.root()
    created = 1                                  # the root counts as created
    frontier = [root]                            # a plain list used as a stack (LIFO)
    while frontier:
        node = frontier.pop()                    # take the most recently added node
        if problem.is_goal(node.state):          # goal test when node is expanded
            return node.state, created, node.path()
        # expand() gives children in ascending order; push them in REVERSE so the
        # smallest node number ends up on top of the stack and is expanded first
        for child in reversed(problem.expand(node)):
            if node.on_path(child.state):        # skip cycles
                continue
            created += 1
            frontier.append(child)
    return None, created, []