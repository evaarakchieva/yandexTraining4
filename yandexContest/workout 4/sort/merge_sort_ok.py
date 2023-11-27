n = int(input())
a = list(map(int, input().split()))

def merge(first_input, second_input):
    sorted_array = []
    l, r = 0, 0
    first_length = len(first_input)
    second_length = len(second_input)
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
        sorted_array.extend(second_input[r:])
    elif r == second_length:
        sorted_array.extend(first_input[l:])
    else:
        return sorted_array

    return sorted_array

def merge_sort(input_array):
    size = len(input_array)
    if size <= 1:
        return input_array
    else:
        mid = size // 2
        first_half = input_array[:mid]
        second_half = input_array[mid:]
        sorted_first_half = merge_sort(first_half)
        sorted_second_half = merge_sort(second_half)
        sorted_array = merge(sorted_first_half, sorted_second_half)
        return sorted_array

result = merge_sort(a)

print(' '.join(map(str, result)))