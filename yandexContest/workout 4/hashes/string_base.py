# string s was created by repeatedly writing the same string t in a row we need to find the minimum length of t
    # so we need to find the maximum value of z[i] where i is not equal to 0 and z[i] is equal to n - i
    # because z[i] is the length of the longest common prefix of s and the suffix of s starting at i
    # so if z[i] is equal to n - i then the suffix of s starting at i is equal to the prefix of s
    # so the string s was created by repeatedly writing the same string t in a row
    # so the minimum length of t is equal to n - i
    # so we need to find the maximum value of n - i where i is not equal to 0 and z[i] is equal to n - i

def find_original_length_with_z_func(input_string):
    n = len(input_string)
    z = [0] * n
    l, r = 0, 0
    original_string_length = n
    maximum_value = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and input_string[z[i]] == input_string[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
        if z[i] == n - i:
            if n - i > maximum_value:
                maximum_value = n - i
    if maximum_value == 0:
        return original_string_length
    return original_string_length - maximum_value

s = input()
res = find_original_length_with_z_func(s)
print(res)