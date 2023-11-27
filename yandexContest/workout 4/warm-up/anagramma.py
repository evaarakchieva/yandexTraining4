first_word = input()
second_word = input()

dict1 = {}
dict2 = {}

for symb in first_word:
    if symb not in dict1:
        dict1[symb] = 0
    dict1[symb] += 1

for symb in second_word:
    if symb not in dict2:
        dict2[symb] = 0
    dict2[symb] += 1

if dict1 == dict2:
    print('YES')
else:
    print('NO')

# еще можно неэффективно стандартной сортирвокой (N logN)  отсортировать обе строки и сравнить