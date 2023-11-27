def compare_strings(input_request, h, x_pow, p_value=10 ** 9 + 7):
    l, a, b = input_request[0], input_request[1] + 1, input_request[2] + 1
    if ((h[a + l - 1] + h[b - 1] * x_pow[l]) % p_value) == ((h[b + l - 1] + h[a - 1] * x_pow[l]) % p_value):
        return 'yes'
    return 'no'

s = input()
q = input()
if len(s) > 0:
    n = len(s)
    x_ = 263
    p = 10 ** 9 + 7
    hashes = [0] * (n + 1)
    x = [0] * (n + 1)
    x[0] = 1
    s = ' ' + s
    for i in range(1, n + 1):
        hashes[i] = (hashes[i - 1] * x_ + ord(s[i])) % p
        x[i] = (x[i - 1] * x_) % p
    for r in range(int(q)):
        request = list(map(int, input().split()))
        if len(request) == 3:
            print(compare_strings(request, hashes, x, p))
