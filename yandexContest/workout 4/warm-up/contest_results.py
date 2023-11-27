def results_analyze(first_group, second_group, tasks_number):
    min_second_group = second_group // tasks_number
    if second_group % tasks_number != 0:
        min_second_group += 1
    if min_second_group < first_group:
        print("Yes")
    else:
        print("No")


a = int(input())
b = int(input())
n = int(input())

results_analyze(a, b, n)