def generate_permutation(arr):
    i = len(arr) - 2
    # find the first element from the end that is less than the next element
    # if there is no such element, the array is the last permutation
    # and we return None
    while i >= 0 and arr[i] >= arr[i + 1]:
        # if arr[i] >= arr[i + 1], then arr[i + 1:] is in descending order
        i -= 1
    # if i == -1, then the array is the last permutation
    if i == -1:
        return None
    # find the first element from the end that is greater than arr[i]
    j = len(arr) - 1
    # if arr[i] >= arr[i + 1], then arr[i + 1:] is in descending order
    # so we can find the first element from the end that is greater than arr[i]
    # by finding the first element from the end that is less than arr[i]
    # and then swapping it with arr[i]
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    # reverse arr[i + 1:]
    # arr[i + 1:] is in descending order
    # so we can reverse it to get the smallest permutation
    # that is greater than the current one
    arr[i + 1:] = reversed(arr[i + 1:])
    # return the next permutation
    return arr

n = int(input())
# start_arr is the first permutation
start_arr = list(range(1, n + 1))
# print all permutations
while start_arr is not None:
    print(''.join(map(str, start_arr)))
    # generate the next permutation
    # if the current permutation is the last one, then start_arr is None
    start_arr = generate_permutation(start_arr)