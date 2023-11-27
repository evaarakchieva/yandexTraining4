def is_possible(test_case):
    n, a, b = test_case
    if n % a <= (n // a) * (b - a):
        return True
    return False

t = int(input())
test_cases = []
for test in range(t):
    if is_possible(list(map(int, input().split()))):
        print('YES')
    else:
        print('NO')