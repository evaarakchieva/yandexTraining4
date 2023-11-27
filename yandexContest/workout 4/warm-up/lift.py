# floors is a number of floors in the building except the 0 floor
# people_per_floor is a list of people on each floor
# max_people_in_lift is a maximum number of people in the lift
# tm is a minimum time in seconds that the lift will spend to deliver all people to the 0 floor
# at first lift is on the 0 floor
# the lift moves with a speed of one floor per second
# the lift can take people from the floor only if there are no more than max_people_in_lift people on the floor

def lift(max_people_in_lift, people_per_floor):
    current, time, weight = len(people_per_floor) - 1, 0, 0
    while current >= 0:
        if people_per_floor[current] // max_people_in_lift > 0:
            time += people_per_floor[current] // max_people_in_lift * (current + 1) * 2
            people_per_floor[current] %= max_people_in_lift
            while people_per_floor[current] == 0 and current >= 0:
                current -= 1
        elif people_per_floor[current] > 0:
            weight += people_per_floor[current]
            time += (current + 1) * 2
            people_per_floor[current] = 0
            while people_per_floor[current] == 0 and current >= 0:
                current -= 1
            while weight < max_people_in_lift and current >= 0:
                if people_per_floor[current] > max_people_in_lift - weight:
                    people_per_floor[current] -= max_people_in_lift - weight
                    weight += max_people_in_lift - weight
                else:
                    weight += people_per_floor[current]
                    people_per_floor[current] = 0
                    current -= 1
        else:
            current -= 1
        weight = 0
    return time

k = int(input())
n = int(input())
a = []
for j in range(n):
    a.append(int(input()))

print(lift(k, a))