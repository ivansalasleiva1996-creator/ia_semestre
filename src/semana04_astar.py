import heapq

GRID = [
    ".....",
    ".###.",
    "...#.",
    ".#...",
    ".....",
]
START, GOAL = (0, 0), (4, 4)

def h(a, b):
    """Heurística Manhattan (admisible y consistente para movimientos ortogonales)."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(node):
    r, c = node
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < len(GRID) and 0 <= nc < len(GRID[0]) and GRID[nr][nc] != '#':
            yield (nr, nc)

def astar(start, goal):
    frontier = [(0, start)]
    came_from = {start: None}
    cost = {start: 0}
    
    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            break
            
        for nxt in neighbors(current):
            new_cost = cost[current] + 1
            if nxt not in cost or new_cost < cost[nxt]:
                cost[nxt] = new_cost
                priority = new_cost + h(nxt, goal)
                heapq.heappush(frontier, (priority, nxt))
                came_from[nxt] = current
                
    if goal not in came_from:
        return None, None
        
    path, cur = [], goal
    while cur is not None:
        path.append(cur)
        cur = came_from[cur]
    path.reverse()
    return path, cost[goal]

def print_grid_with_path(grid, path):
    """Imprime el mapa marcando la ruta encontrada con '*'."""
    path_set = set(path) if path else set()
    print("\nVisualización del Mapa:")
    for r, row in enumerate(grid):
        line = []
        for c, val in enumerate(row):
            if (r, c) == START: line.append("S")
            elif (r, c) == GOAL: line.append("G")
            elif (r, c) in path_set: line.append("*")
            else: line.append(val)
        print(" ".join(line))

if __name__ == "__main__":
    path, total_cost = astar(START, GOAL)
    print("=" * 50)
    print("BÚSQUEDA A* OPTIMIZADA")
    print("=" * 50)
    print("Ruta:", path)
    print("Costo total:", total_cost)
    print_grid_with_path(GRID, path)