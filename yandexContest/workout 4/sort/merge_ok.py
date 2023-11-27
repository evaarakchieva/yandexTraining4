n = int(input())
first_array = list(map(int, input().split()))

m = int(input())
second_array = list(map(int, input().split()))


def merge_sort(first_length, first_input, second_length, second_input):
    sorted_array = []
    l, r = 0, 0
    while l < first_length and r < second_length:
        if first_input[l] > second_input[r]:
            sorted_array.append(second_input[r])
            r = r + 1
        elif first_input[l] < second_input[r]:
            sorted_array.append(first_input[l])
            l = l + 1
        else:
            sorted_array.append(first_input[l])
            l = l + 1
    if l == first_length:
        sorted_array.extend(second_array[r:])
    elif r == second_length:
        sorted_array.extend(first_array[l:])
    else:
        return sorted_array

    return sorted_array


result = merge_sort(n, first_array, m, second_array)

print(' '.join(map(str, result)))