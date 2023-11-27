def count_max_square(n_size, m_size, carrots):
    dp = [[0] * m_size for _ in range(n_size)]
    max_len = 0
    for i in range(n_size):
        dp[i][0] = carrots[i][0]
        max_len = max(max_len, dp[i][0])
    for j in range(m_size):
        dp[0][j] = carrots[0][j]
        max_len = max(max_len, dp[0][j])
    for i in range(1, n_size):
        for j in range(1, m_size):
            if carrots[i][j] == 1:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_len = max(max_len, dp[i][j])
    return max_len


n, m = map(int, input().split())
input_matrix = [list(map(int, input().split())) for _ in range(n)]

print(count_max_square(n, m, input_matrix))


