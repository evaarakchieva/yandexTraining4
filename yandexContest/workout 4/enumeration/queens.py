def check_neighbours(dinosaurs, row, col):
    for r, c in dinosaurs:
        if row == r or col == c or row + col == r + c or row - col == r - c:
            return 0
    return 1

def arrange_recursive(n, dinosaurs, col):
    if col == n:
        return 1
    count_solutions = 0
    for i in range(n):
        if check_neighbours(dinosaurs, i, col):
            dinosaurs.append((i, col))
            count_solutions += arrange_recursive(n, dinosaurs, col + 1)
            dinosaurs.pop()
    return count_solutions

def arrange_n_dinosaurs(n):
    dinosaurs = []
    return arrange_recursive(n, dinosaurs, 0)

input_n = int(input())
print(arrange_n_dinosaurs(input_n))