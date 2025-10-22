import numpy as np

def format(matrix):
    for i in range(3):
        for j in range(3):
            if j != 2:
                print(matrix[i][j], "|", end="")
            else:
                print(matrix[i][j])
        for k in range(7):
            print("-", end="")
        print("\n")

def check_combination(matrix):
    winning_combinations = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [1, 5, 9],
        [3, 5, 7]
    ]

    for player in ['X', 'O']:
        for combo in winning_combinations:
            row1, col1 = (combo[0] - 1) // 3, (combo[0] - 1) % 3
            row2, col2 = (combo[1] - 1) // 3, (combo[1] - 1) % 3
            row3, col3 = (combo[2] - 1) // 3, (combo[2] - 1) % 3

            if (matrix[row1][col1] == player and
                matrix[row2][col2] == player and
                matrix[row3][col3] == player):
                return player

    for row in matrix:
        for cell in row:
            if cell == '':
                return ''

    return 'Tie'

matrix = np.full((3, 3), '', dtype=str)
print("FIRST TURN OF X")
print("SECOND TURN OF O")

Winner = ''
i = 1
sign = ''
while Winner not in ['Tie', 'X', 'O']:
    row = int(input("Enter Row number (0-2): "))
    col = int(input("Enter Col number (0-2): "))

    if i % 2 != 0:
        sign = 'X'
    else:
        sign = 'O'

    if matrix[row][col] != '':
        print("Alert!, Player has already marked there")
        continue
    else:
        matrix[row][col] = sign
        format(matrix)
        Winner = check_combination(matrix)
        i += 1

print("Winner is", Winner)