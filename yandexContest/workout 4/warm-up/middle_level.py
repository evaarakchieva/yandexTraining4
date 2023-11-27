def count_dissatisfaction(input_array_length, input_array):
    array_of_dissatisfaction = [0] * input_array_length
    for i in range(input_array_length):
        sum_of_right = 0
        for j in range (i + 1, input_array_length):
            sum_of_right += input_array[j]
        array_of_dissatisfaction[i] += (sum_of_right - input_array[i] * (input_array_length - i - 1))
        sum_of_left = 0
        for k in range(i):
            sum_of_left += input_array[k]
        array_of_dissatisfaction[i] += (input_array[i] * i - sum_of_left)
    return array_of_dissatisfaction

# n = int(input())
# input_arr = list(map(int, input().split()))
# print(' '.join(map(str, count_dissatisfaction(n, input_arr))))

# частичные префиксные суммы
def count_dissatisfaction_optimized(people_count, ratings):
    res = []
    lower_sum = 0
    lower_len = 1
    higher_sum = sum(ratings)
    higher_len = people_count
    for st in range(n):
        lower_sum += ratings[st]
        left_dissatisfaction = lower_len * ratings[st] - lower_sum
        right_dissatisfaction = higher_sum - ratings[st] * higher_len
        lower_len += 1
        higher_len -= 1
        higher_sum -= ratings[st]
        res.append(str(left_dissatisfaction + right_dissatisfaction))
    return res

n = int(input())
input_arr = list(map(int, input().split()))
print(' '.join(count_dissatisfaction_optimized(n, input_arr)))