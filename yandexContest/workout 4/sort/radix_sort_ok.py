n = int(input())
initial_array = []
sorted_array = []

for i in range(n):
    number = input()
    initial_array.append(number)

print('Initial array:')
print(', '.join(map(str, initial_array)))

count_digits = len(initial_array[0])

for phase in range(1, count_digits + 1):
    buckets = [[]] * 10
    print('**********')
    print(f'Phase {phase}')

    for i in range(n):
        current_number = initial_array[i]
        digit = int(current_number[-phase])
        buckets[digit] = buckets[digit] + [current_number]

    initial_array = []

    for index, value in enumerate(buckets):
        bucket = ', '.join(map(str, value))
        if bucket:
            print(f"Bucket {index}: {bucket}")
        else:
            print(f"Bucket {index}: empty")
        initial_array.extend(value)

print('**********')
print('Sorted array:')
print(', '.join(map(str, initial_array)))