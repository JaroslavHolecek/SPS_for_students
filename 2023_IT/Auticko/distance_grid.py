def spread_distances(grid, goal_value=0, obstacle_value=2, max_iterations=1000):
    """
    Iterativně přiřazuje každé buňce vzdálenost od cílových buněk (označených goal_value),
    bez použití BFS – pouze opakovaným procházením celé mřížky.

    grid: 2D list (int) – vstupní mapa
    goal_value: hodnota cílové buňky (defaultně 0)
    obstacle_value: hodnota nepřístupné buňky (defaultně 2)
    max_iterations: maximální počet iterací (ochrana proti nekonečné smyčce)

    Vrací:
    - 2D list s přiřazenými vzdálenostmi (cíle = 0, překážky = obstacle_value, ostatní >= 1)
    """
    height = len(grid)
    width = len(grid[0])
    dist = [[float('inf') for _ in range(width)] for _ in range(height)]

    last_assigne = []
    neigbohrs = []
    # Inicializace cílových pozic
    for y in range(height):
        for x in range(width):
            if grid[y][x] == goal_value:
                dist[y][x] = 0
                last_assigne.append((y,x))
            elif grid[y][x] == obstacle_value:
                dist[y][x] = obstacle_value  # překážky zůstanou konstantní

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for 

    for _ in range(max_iterations):
        changed = False
        for y in range(height):
            for x in range(width):
                if dist[y][x] == obstacle_value:
                    continue
                min_neigh = float('inf')
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < width and 0 <= ny < height:
                        if dist[ny][nx] != obstacle_value:
                            min_neigh = min(min_neigh, dist[ny][nx])
                if min_neigh + 1 < dist[y][x]:
                    dist[y][x] = min_neigh + 1
                    changed = True
        if not changed:
            break

    return dist
