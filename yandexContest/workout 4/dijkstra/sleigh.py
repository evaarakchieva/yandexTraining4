import heapq
from collections import deque

def dijkstra(matrix, start):
    distances = {vertex: [float('infinity'), 0] for vertex, _ in enumerate(matrix[1:], start=1)}
    distances[start][0] = 0
    queue = [(0, start)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex][0]:
            continue
        for neighbor, weight in enumerate(matrix[current_vertex][1:], start=1):
            if weight <= 0:
                continue
            distance = current_distance + weight
            if distance < distances[neighbor][0]:
                distances[neighbor][0] = distance
                distances[neighbor][1] = current_vertex
                heapq.heappush(queue, (distance, neighbor))
    maximum_distance = max(distances.items(), key=lambda info: info[1][0])[1][0]
    remoted_city = max(distances.items(), key=lambda info: info[1][0])[0]
    route = []
    city_now = remoted_city
    while city_now != 1:
        route.append(city_now)
        city_now = distances[city_now][1]
    else:
        route.append(city_now)
    return maximum_distance, route

def bfs(graph, city):
    visited_cities = {city: 0}
    queue = deque([(0, city)])
    while queue:
        distance, current_city = queue.popleft()
        for neighbor, road_length in graph[current_city]:
            new_distance = distance + road_length
            if neighbor not in visited_cities or new_distance < visited_cities[neighbor]:
                queue.append((new_distance, neighbor))
                visited_cities[neighbor] = new_distance
                matrix[city][neighbor] = visited_cities[neighbor] / speeds[neighbor] + preparation_time[neighbor]

n = int(input())
preparation_time, speeds = [0], [0]
graph = {}
matrix = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n):
    time, pace = map(int, input().split())
    preparation_time.append(time)
    speeds.append(pace)

for _ in range(n - 1):
    a, b, s = map(int, input().split())
    graph.setdefault(a, []).append((b, s))
    graph.setdefault(b, []).append((a, s))

for city in graph:
    bfs(graph, city)

res = dijkstra(matrix, 1)
print(f'{res[0]:.10f}')
print(*res[1])