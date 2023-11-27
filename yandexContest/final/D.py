def find_min_len_subseq(length, min_len_sums_dict):
    min_len = float('inf')
    min_subsequence = None
    for a_sum, a_bricks in min_len_sums_dict.items():
        b_sum = length - a_sum
        if b_sum in min_len_sums_dict:
            b_bricks = min_len_sums_dict[b_sum]
            total_len = len(b_bricks) + len(a_bricks)
            if total_len < min_len:
                min_subsequence = b_bricks + a_bricks
                min_len = total_len
    return min_subsequence

def min_len_sums_calc(bricks):
    dp_calc_set = {0}
    min_len_sums_dict = {0 :[]}
    for first_brick in bricks:
        new_sums_set = dp_calc_set.copy()
        for second_brick in sorted(dp_calc_set, reverse=True):
            new_sum = first_brick + second_brick
            new_sums_set.add(new_sum)
            new_subset = [first_brick] + min_len_sums_dict[second_brick]
            if new_sum not in min_len_sums_dict:
                min_len_sums_dict[new_sum] = new_subset
            else:
                min_len_sums_dict[new_sum] = min(min_len_sums_dict[new_sum], new_subset, key=len)
        dp_calc_set = new_sums_set
    return min_len_sums_dict

def find_solution(length, brick_type, bricks):
    if length > sum(bricks) * 2:
        return -1
    min_len_sums_dict = min_len_sums_calc(bricks)
    min_subsequence = find_min_len_subseq(length, min_len_sums_dict)
    if not min_subsequence:
        return 0
    answer = ' '.join(map(str, min_subsequence))
    return f"{len(min_subsequence)}\n{answer}"

input_length, input_brick_type = map(int, input().split())
input_bricks = list(map(int, input().split()))
print(find_solution(input_length, input_brick_type, input_bricks))