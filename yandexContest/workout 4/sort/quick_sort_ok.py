import random

def quick_sort(array, l, r):
    if l < r:
        x = random.choice(array[l:r + 1])
        equal, greater = partition(array, l, r, x)
        quick_sort(array, l, equal)
        quick_sort(array, greater, r)

def partition(array, l, r, x):
    equal, greater, current = l, l, l
    while current < r:
        if array[current] < x:
            buffer = array[current]
            array[current] = array[greater]
            array[greater] = array[equal]
            array[equal] = buffer
            equal += 1
            greater += 1
        elif array[current] == x:
            buffer = array[current]
            array[current] = array[greater]
            array[greater] = buffer
            greater += 1
        current += 1
    return equal, greater

n = int(input())
if n > 0:
    a = list(map(int, input().split()))
    quick_sort(a, 0, n)
    print(' '.join(map(str, a)))