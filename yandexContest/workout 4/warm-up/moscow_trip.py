import math
def length_of_circular_arcs(distance, x1, y1, x2, y2):
    central_angle_between_two_dots = math.atan2(x1 * y2 - x2 * y1, x1 * x2 + y1 * y2)
    if central_angle_between_two_dots < 0:
        central_angle_between_two_dots += 2 * math.pi
    if central_angle_between_two_dots > math.pi:
        central_angle_between_two_dots = 2 * math.pi - central_angle_between_two_dots
    length_of_the_shortest_circular_arc_between_two_dots = distance * central_angle_between_two_dots
    return length_of_the_shortest_circular_arc_between_two_dots

def find_shortest_path_from_a_to_b(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0

    distance_ao = math.sqrt(x1 ** 2 + y1 ** 2)
    distance_ob = math.sqrt(x2 ** 2 + y2 ** 2)

    if x1 == 0 and y1 == 0:
        return distance_ob
    if x2 == 0 and y2 == 0:
        return distance_ao
    if x1 == (-1) * x2 and y1 == (-1) * y2:
        return distance_ao + distance_ob
    if distance_ao == distance_ob:
        return min(length_of_circular_arcs(distance_ao, x1, y1, x2, y2), distance_ao * 2)
    elif distance_ao > distance_ob:
        p1 = (distance_ao - distance_ob) + length_of_circular_arcs(distance_ob, x1, y1, x2, y2)
        greater_arc = length_of_circular_arcs(distance_ao, x1, y1, x2, y2)
        return min(p1, greater_arc + (distance_ao - distance_ob), (distance_ao + distance_ob))
    elif distance_ao < distance_ob:
        p1 = (distance_ao + distance_ob)
        greater_arc = length_of_circular_arcs(distance_ao, x1, y1, x2, y2)
        return min(p1,greater_arc + (distance_ob - distance_ao))

input_array = list(map(int, input().split()))
if len(input_array) == 4:
    print(find_shortest_path_from_a_to_b(input_array[0], input_array[1], input_array[2], input_array[3]))