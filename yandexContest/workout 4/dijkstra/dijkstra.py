def dijkstra(n_strings, start, finish, adjacency_matrix):
    infinity = 10 ** 9
    distances = [infinity] * n_strings
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
                    queue.append(adjacent_vertex)
    if distances[finish - 1] == infinity:
        return -1
    return distances[finish - 1]

n, s, f = map(int, input().split())
matrix = []
for _ in range(n):
    matrix_str = list(map(int, input().split()))
    matrix.append(matrix_str)

print(dijkstra(n, s, f, matrix))
