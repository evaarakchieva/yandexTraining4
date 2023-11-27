def mirror_z_function():
    string_length = int(input())
    input_string = input()
    x_value = 263
    p_value = 10**9 + 7
    x_pow = [1] * (string_length + 1)
    hashes = [0] * (string_length + 1)
    hashes_mirrored = [0] * (string_length + 1)
    x_backward_powers = [1] * (string_length + 1)
    ord_input_string = [ord(ch) for ch in input_string]
    result = [0] * string_length

    def compare_by_hash(s1, s2, length):
        return (
            (hashes[s1 + length] + hashes_mirrored[s2 + 1] * x_pow[length]) % p_value
            == (hashes_mirrored[s2 - length + 1] + hashes[s1] * x_pow[length]) % p_value
        )

    def find_maximum_mirrored_part(high):
        res = 0
        low = 0
        s2 = high
        while low <= high:
            mid = low + (high - low) // 2
            if compare_by_hash(0, s2, s2 - mid + 1):
                res = s2 - mid + 1
                high = mid - 1
            else:
                low = mid + 1
        return res

    for i in range(1, string_length + 1):
        x_pow[i] = (x_pow[i - 1] * x_value) % p_value
        x_backward_powers[string_length - i] = (x_backward_powers[string_length - i + 1] * x_value) % p_value
        hashes[i] = (hashes[i - 1] * x_value + ord_input_string[i - 1]) % p_value
        hashes_mirrored[string_length - i] = (
            hashes_mirrored[string_length - i + 1] * x_value + ord_input_string[string_length - i]
        ) % p_value

    for i in range(string_length):
        result[i] = find_maximum_mirrored_part(i)

    return result

answer = mirror_z_function()
print(' '.join(map(str, answer)))