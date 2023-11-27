def count_c_x(x):
    i, j = 1, 1
    i_2, j_3 = 1, 1
    k = 1
    ans = 0
    while k <= x:
        if i_2 == j_3:
            i += 1
            i_2 = i*i
            k -= 1
        elif i_2 < j_3:
            ans = i_2
            i += 1
            i_2 = i*i
        else:
            ans = j_3
            j += 1
            j_3 = j*j*j
        k += 1
    return ans

print(count_c_x(int(input())))