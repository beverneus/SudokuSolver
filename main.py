sudoku = [[0,5,3,0,3,9,0,0,6],
          [6,0,2,7,1,0,0,0,5],
          [0,0,7,5,0,0,0,0,8],
          [1,9,0,0,0,0,0,2,0],
          [0,3,0,0,8,0,0,6,0],
          [2,0,0,0,7,4,8,1,0],
          [0,0,0,0,0,6,4,0,7],
          [0,0,0,8,0,2,6,0,0],
          [3,8,0,0,0,0,9,0,0]]

def find_empty(matrix):
    empty_list = []
    a = 0
    for i in matrix:
        b = 0
        for j in i:
            if j == 0:
                empty_list.append((a, b))
            b += 1
        a += 1
    return empty_list

def backtrack(empty_list, matrix, i, u):
    location = empty_list[i]
    matrix[location[0]][location[1]] += 1
    if u != 1:
        backtrack(empty_list, matrix, 0, 1)
    print(matrix[location[0]][location[1]])

def main():
    empty_list = find_empty(sudoku)
    backtrack(empty_list, sudoku, 0, 0)


if __name__ == "__main__":
    main()
