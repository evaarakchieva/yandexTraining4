def count_palindrome_substrings(input_string):
    n = len(input_string)
    if n == 0:
        return 0

    # Преобразуем строку для работы с нечетными и четными палиндромами
    modified_string = '#' + '#'.join(input_string) + '#'

    n = len(modified_string)
    p = [0] * n
    c = r = 0

    for i in range(n):
        if i <= r:
            mirror = 2 * c - i
            p[i] = min(r - i, p[mirror])

        # Расширяем палиндромную центральную точку
        a, b = i + (1 + p[i]), i - (1 + p[i])

        while a < n and b >= 0 and modified_string[a] == modified_string[b]:
            p[i] += 1
            a, b = a + 1, b - 1

        # Обновляем центральную точку и границу
        if i + p[i] > r:
            c, r = i, i + p[i]

    # Теперь p содержит длины палиндромных подстрок с учетом '#'
    count = 0
    for length in p:
        # Для каждой длины палиндромной подстроки, количество палиндромов увеличивается на (length + 1) // 2
        count += (length + 1) // 2

    return count

s = input()
print(count_palindrome_substrings(s))