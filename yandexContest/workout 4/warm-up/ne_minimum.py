def ne_minimum(input_array, input_request):
    l, r = input_request[0], input_request[1]
    minimum = a[l]
    for j in range(l, r + 1):
        if input_array[j] < minimum:
            minimum = input_array[j]
    for k in range(l, r + 1):
        if input_array[k] != minimum:
            return input_array[k]
    return 'NOT FOUND'

first_string = list(map(int, input().split()))
a = list(map(int, input().split()))
if len(first_string) == 2 and len(a) == first_string[0] and len(a) > 0:
    for i in range(first_string[1]):
        request = list(map(int, input().split()))
        if len(request) == 2:
            print(ne_minimum(a, request))
