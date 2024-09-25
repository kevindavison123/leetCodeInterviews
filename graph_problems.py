from collections import deque
from typing import List


def printGraph(vertices: int, edges: List[List[int]]) -> List[List[int]]:
    graph = [[] for i in range(vertices)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    return graph


def bfs_graph(graph: List[List[int]], start: int) -> List[int]:
    visited = [False] * len(graph)
    queue = []
    for i in range(start):
        if not visited[i]:
            queue.append(i)
            visited[i] = True
            while queue:
                node = queue.pop(0)
                print(node, end=" ")
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        queue.append(neighbor)
                        visited[neighbor] = True


def dfs(node, adj, visited, values):
    visited[node] = True
    values.append(node)
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited, values)


def dfs_graph(graph: List[List[int]], size: int) -> List[int]:
    visited = [False] * size
    values = []
    dfs(0, graph, visited, values)
    return values


def find_path_exist(grid: List[List[int]]) -> bool:
    # The grid is-
    # 3 0 3 0 0
    # 3 0 0 0 3
    # 3 3 3 3 3
    # 0 2 3 0 0
    # 3 0 0 1 3
    # No path exists
    visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    row, col = 0, 0
    # find source cell 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                row, col = i, j
                break
    return grid_dfs(row, col, grid, visited)


def grid_dfs(row, col, grid, visited):
    # check if bounds or wall
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
        return False
    if grid[row][col] == 2:
        return True
    if visited[row][col]:
        return False
    visited[row][col] = True
    return (grid_dfs(row + 1, col, grid, visited)
            or grid_dfs(row - 1, col, grid, visited)
            or grid_dfs(row, col + 1, grid, visited)
            or grid_dfs(row, col - 1, grid, visited))


def isValid(x, y, size):
    return (x >= 0 and x < size and y >= 0 and y < size)


def knight_move(knight_pos, target_pos, size):
    visited = [[False for i in range(size)] for j in range(size)]
    knight_pos[0] -= 1
    knight_pos[1] -= 1
    target_pos[0] -= 1
    target_pos[1] -= 1
    dxy = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]
    q = deque()
    q.append([knight_pos[0], knight_pos[1], 0])
    visited[knight_pos[0]][knight_pos[1]] = True
    while len(q):
        cur = q.popleft()
        x = cur[0]
        y = cur[1]
        steps = cur[2]
        if x == target_pos[0] and y == target_pos[1]:
            return steps
        for i in range(len(dxy)):
            next_x = x + dxy[i][0]
            next_y = y + dxy[i][1]
            if isValid(next_x, next_y, size) and visited[next_x][next_y] == False:
                visited[next_x][next_y] = True
                q.append([next_x, next_y, steps + 1])
                visited[next_x][next_y] = True
    return -1


if __name__ == '__main__':
    vertices = 5
    edges = {(0, 1), (0, 4), (4, 1), (4, 3), (1, 3), (1, 2), (3, 2)}
    print(printGraph(vertices, edges))
    vertices = 4
    edges = {(0, 3), (0, 2), (2, 1)}
    print(printGraph(vertices, edges))
    vertices = 5
    # adj = {{1, 2, 3}, {}, {4}, {}, {}}
    adj = [[1, 2, 3], [], [4], [], []]
    print(bfs_graph(adj, 5))
    adj = [[1, 2], [], []]
    print(bfs_graph(adj, 3))
    adj = [[2, 3, 1], [0], [0, 4], [0], [2]]
    print(dfs_graph(adj, 5))
    grid = [[3, 0, 3, 0, 0], [3, 0, 0, 0, 3], [3, 3, 3, 3, 3], [0, 2, 3, 0, 0], [3, 0, 0, 1, 3]]
    print(find_path_exist(grid))
    grid = [[1, 3], [3, 2]]
    print(find_path_exist(grid))

