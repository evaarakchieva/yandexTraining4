import heapq

def quick_dijkstra(n, start, finish, adjacency_list):
    distances = {vertex: float('inf') for vertex in range(1, n+1)}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current = heapq.heappop(queue)
        if current_distance > distances[current]:
            continue
        for adjacent_vertex, edge_weight in adjacency_list[current]:
            new_distance = distances[current] + edge_weight
            if new_distance < distances[adjacent_vertex]:
                distances[adjacent_vertex] = new_distance
                heapq.heappush(queue, (new_distance, adjacent_vertex))
    if distances[finish] == float('inf'):
        return -1
    return distances[finish]

input_n, k = map(int, input().split())
input_adjacency_list = [[] for _ in range(input_n + 1)]
for _ in range(k):
    first_city, second_city, distance = map(int, input().split())
    input_adjacency_list[first_city].append((second_city, distance))
    input_adjacency_list[second_city].append((first_city, distance))

a, b = map(int, input().split())

print(quick_dijkstra(input_n, a, b, input_adjacency_list))
