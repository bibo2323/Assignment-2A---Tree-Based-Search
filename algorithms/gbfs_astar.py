"""GBFS and A* (informed). Owner: <your name>

Use problem.h(state) for the heuristic and node.g for the cost so far.
    GBFS: priority = h(n)
    A*  : priority = g(n) + h(n)
Ties: smaller node number first, then whichever was added first. A priority
queue entry like (priority, state, counter, node) handles this automatically.
"""
import heapq #tool for priority queue. it is a list that gives back smallest item first.


def gbfs(problem): # "problem" is the loaded map(in search.py)
    
    root = problem.root()
    node_count = 1       # the root counts as a created node. starts as 1 because root already exist
    counter = 0          # goes up by 1 for every node added

    frontier = [(problem.h(root.state), root.state, counter, root)]  # (priority, state, counter, node)-> frontier is to-do list of nodes waiting to be expanded. It starts with the root. 

    while frontier:  # keep going when the frontier is not empty
        _, _, _, node = heapq.heappop(frontier) # pulls out smallest priority off frontier
                                                
        if problem.is_goal(node.state): # if the node is a destination, stop and return:
                                        # node.state: (the destination town reached) 
                                        # node_count: (how many nodes were created in total)
                                        # node.path():(the route from origin to here)
            return node.state, node_count, node.path()

        for child in problem.expand(node): #finds outgoing nodes from current node
            if node.on_path(child.state): #if "true", "continue" skips any child already on this path and moves to the next child.
             continue
            node_count += 1
            counter += 1
            # GBFS only looks at estimated distance left (h), cost is not main priority
            priority = problem.h(child.state)
            heapq.heappush(frontier, (priority, child.state, counter, child)) # adds the child to the frontier. The heap puts it in the right order automatically.

    # If nothing is found, the frontier is empty and no destination was reached. Returns no goal, the node count, and an empty path.
    return None, node_count, []


def astar(problem):

    root = problem.root()
    node_count = 1       # the root counts as a created node. starts as 1 because root already exist
    counter = 0          # goes up by 1 for every node added

    # The root has g = 0, so its priority is just h.
    frontier = [(problem.h(root.state), root.state, counter, root)] # (priority, state, counter, node)

    while frontier:
        # Take the entry with the smallest priority off the frontier
        _, _, _, node = heapq.heappop(frontier)

        if problem.is_goal(node.state): # if the node is a destination, stop and return:
                                        # node.state: (the destination town reached) 
                                        # node_count: (how many nodes were created in total)
                                        # node.path():(the route from origin to here)
            return node.state, node_count, node.path() 

        for child in problem.expand(node):  #finds outgoing nodes from current node
            if node.on_path(child.state): #if "true", "continue" skips any child already on this path and moves to the next child.
                continue
            node_count += 1
            counter += 1
            # A* adds the cost paid so far (g) to the estimated cost left (h)
            priority = child.g + problem.h(child.state)
            heapq.heappush(frontier, (priority, child.state, counter, child)) # adds the child to the frontier. The heap puts it in the right order automatically.

     # If nothing is found, the frontier is empty and no destination was reached. Returns no goal, the node count, and an empty path.
    return None, node_count, []