def sum_fraction(a, b, c, d):
    m = a * d + b * c
    n = b * d
    gcd = 1
    for i in range(1, min(m, n) + 1):
        if m % i == 0 and n % i == 0:
            gcd = i
    print(m // gcd, n // gcd)


input_array = list(map(int, input().split()))
if len(input_array) == 4:
    sum_fraction(input_array[0], input_array[1], input_array[2], input_array[3])

# еще можно использовать алгоритм евклида для нахождения нод