import heapq  # Importing heapq for priority queue operations

def bfs(graph, start, goal):
    """Performs Breadth-First Search (BFS) to find the shortest path in terms of steps."""
    queue = [(start, [start], 0)]  # (Current node, Path taken, Total cost)
    while queue:
        node, path, cost = queue.pop(0)  # Dequeue the first element
        if node == goal:
            return path, cost  # Return the path and cost if goal is found
        for neighbor, weight in graph.get(node, []):
            if neighbor not in path:  # Avoid cycles
                queue.append((neighbor, path + [neighbor], cost + weight))
    return None, float('inf')  # Return infinity if no path is found

def ucs(graph, start, goal):
    """Performs Uniform Cost Search (UCS) using a priority queue to find the least cost path."""
    queue = [(0, start, [start])]  # (Cost, Current node, Path taken)
    heapq.heapify(queue)
    while queue:
        cost, node, path = heapq.heappop(queue)  # Get the lowest-cost node
        if node == goal:
            return path, cost  # Return the path and cost if goal is found
        for neighbor, weight in graph.get(node, []):
            if neighbor not in path:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))
    return None, float('inf')  # Return infinity if no path is found

def greedy_best_first_search(graph, heuristic, start, goal):
    """Performs Greedy Best-First Search using heuristic values to prioritize nodes."""
    queue = [(heuristic[start], start, [start], 0)]  # (Heuristic value, Node, Path, Cost)
    heapq.heapify(queue)
    while queue:
        _, node, path, cost = heapq.heappop(queue)  # Expand the most promising node
        if node == goal:
            return path, cost  # Return the path and cost if goal is found
        for neighbor, weight in graph.get(node, []):
            if neighbor not in path:
                heapq.heappush(queue, (heuristic[neighbor], neighbor, path + [neighbor], cost + weight))
    return None, float('inf')  # Return infinity if no path is found

def iterative_deepening_dfs(graph, start, goal, max_depth=10):
    """Performs Iterative Deepening Depth-First Search (IDDFS)."""
    def dls(node, path, cost, depth):
        if node == goal:
            return path, cost  # Return path and cost if goal is found
        if depth <= 0:
            return None, float('inf')  # Stop exploring if depth limit is reached
        for neighbor, weight in graph.get(node, []):
            if neighbor not in path:
                result, result_cost = dls(neighbor, path + [neighbor], cost + weight, depth - 1)
                if result:
                    return result, result_cost  # Return the found path and cost
        return None, float('inf')
    
    for depth in range(max_depth):  # Increase depth limit iteratively
        result, cost = dls(start, [start], 0, depth)
        if result:
            return result, cost
    return None, float('inf')  # Return infinity if no path is found

# Define the Romania map as an adjacency list
graph = {
    "Arad": [("Zerind", 75), ("Timisoara", 118), ("Sibiu", 140)],
    "Zerind": [("Arad", 75), ("Oradea", 71)],
    "Oradea": [("Zerind", 71), ("Sibiu", 151)],
    "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
    "Timisoara": [("Arad", 118), ("Lugoj", 111)],
    "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
    "Mehadia": [("Lugoj", 70), ("Drobeta", 75)],
    "Drobeta": [("Mehadia", 75), ("Craiova", 120)],
    "Craiova": [("Drobeta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
    "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
    "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
    "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
    "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90)],
}

# Heuristic values for Greedy Best-First Search (straight-line distance to Bucharest)
heuristic = {
    "Arad": 366, "Zerind": 374, "Oradea": 380, "Sibiu": 253, "Timisoara": 329,
    "Lugoj": 244, "Mehadia": 241, "Drobeta": 242, "Craiova": 160, "Rimnicu Vilcea": 193,
    "Fagaras": 176, "Pitesti": 100, "Bucharest": 0, "Giurgiu": 77,
}

# Taking user input for start and goal cities
start = input("Enter the starting location: ")
goal = input("Enter the destination location: ")

# Running each search algorithm and storing results
results = {
    "BFS": bfs(graph, start, goal),
    "UCS": ucs(graph, start, goal),
    "Greedy Best-First Search": greedy_best_first_search(graph, heuristic, start, goal),
    "IDDFS": iterative_deepening_dfs(graph, start, goal)
}

# Sorting results based on path cost in ascending order
sorted_results = sorted(results.items(), key=lambda x: x[1][1])

# Displaying results
print("\nSearch results sorted by cost:")
for method, (path, cost) in sorted_results:
    print(f"{method}: Path = {path}, Cost = {cost}")
