n = int(input())
a = list(map(int, input().split()))
x = int(input())
l, r = 0, 0

for i in a:
    if x > i:
        l += 1
    else:
        r += 1
print(l)
print(r)