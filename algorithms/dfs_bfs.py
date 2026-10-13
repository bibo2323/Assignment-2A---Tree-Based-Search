"""DFS and BFS (uninformed). Owner: ____________

bfs() below is a WORKING EXAMPLE showing the pattern. Copy its style for dfs().
Tie-breaking: problem.expand() already returns children in ascending node order.
BFS = queue (first in, first out).  DFS = stack (last in, first out), so for DFS
you must push children in REVERSE order to expand the smallest node first.
"""
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
    # TODO: implement depth-first search (see note at the top of the file)
    raise NotImplementedError("DFS not implemented yet")
