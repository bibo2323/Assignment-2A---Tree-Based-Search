# COS30019 A2A - Route Finding (Tree-Based Search)

## Run
    python search.py <filename> <method>
    python search.py tests\PathFinder-test.txt BFS
Methods: DFS, BFS, GBFS, AS, CUS1, CUS2  (or use search.bat on Windows)

## Batch test (all methods x all files, saves results.csv)
    python run_all.py tests results.csv

## Files
- search.py          command-line entry + output format
- problem.py         parser, Problem (graph) and SearchNode classes
- algorithms/        dfs_bfs.py, gbfs_astar.py, custom.py (one file per person)
- run_all.py         batch tester for the Testing / Insights sections
- tests/             test case files (.txt)

## Rules for every algorithm
1. One function per method: def name(problem)
2. Return (goal, nodes_created, path); if no goal: (None, nodes_created, [])
3. Use problem.root(), problem.expand(node), problem.is_goal(state), problem.h(state)
4. Count the root as a created node; add len(children) each time you expand
5. Tie-break: smaller node number first, then the one added first
6. Stop when the first goal node is expanded
