def dijkstra_with_path(n_strings, start, finish, adjacency_matrix):
    infinity = 10 ** 9
    distances = [infinity] * n_strings
    prev_vertices = [-1] * n_strings
    # distances is a list of distances from the start vertex to all other vertices
    distances[start - 1] = 0
    # queue is a list of vertices that need to be checked
    queue = [start - 1]
    while queue:
        current = queue.pop(0)
        for adjacent_vertex in range(n_strings):
            if adjacency_matrix[current][adjacent_vertex] != -1:
                if distances[adjacent_vertex] > distances[current] + adjacency_matrix[current][adjacent_vertex]:
                    distances[adjacent_vertex] = distances[current] + adjacency_matrix[current][adjacent_vertex]
                    prev_vertices[adjacent_vertex] = current
                    queue.append(adjacent_vertex)
    if distances[finish - 1] == infinity:
        return -1
    if distances[finish - 1] == 1:
        return [start, finish]
    path = []
    current = finish - 1
    while current != -1:
        path.append(current + 1)
        current = prev_vertices[current]
    return path[::-1]


n, s, f = map(int, input().split())
matrix = []
for _ in range(n):
    matrix_str = list(map(int, input().split()))
    matrix.append(matrix_str)

result = dijkstra_with_path(n, s, f, matrix)
if result == -1:
    print(result)
else:
    print(' '.join(map(str, result)))
