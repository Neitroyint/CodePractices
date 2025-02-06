def main():
    cols: int = 3
    rows: int = 4
    matrix: list[list[int]] = [[0 for c in range(cols)] for r in range(rows)]

    matrix[0][0], matrix[0][1], matrix[0][2] = 1, 2, 3
    matrix[1][0], matrix[1][1], matrix[1][2] = 4, 5, 6
    matrix[2][0], matrix[2][1], matrix[2][2] = 7, 8, 9

    print_matrix(matrix)

    new_matrix: list[list[int]] = [[0 for c in range(rows)] for r in range(cols)]

    for i_row, row in enumerate(matrix):
        for i_col, col in enumerate(row):
            # n_row, n_col = turn_matrix_left_pos(i_row, i_col, cols)
            n_row, n_col = turn_matrix_right_pos(i_row, i_col, rows)
            new_matrix[n_row][n_col] = col

    print('---'*4)
    print('Result')
    print('---'*4)
    print_matrix(new_matrix)

def turn_matrix_left_pos(row: int, col: int, cols: int) -> tuple[int, int]:
    return cols-1-col, row

def turn_matrix_right_pos(row: int, col: int, rows: int) -> tuple[int, int]:
    return col, rows-1-row


def print_matrix(matrix: list[list[int]]) -> None:
    max_chars: int = get_matrix_max_chars(matrix)

    for row in matrix:
        print_row: str = '|'
        for col in row:
            field_text: str = ' ' + ' ' * (max_chars - len(str(col))) + str(col) + ' '
            print_row +=  f'{field_text}|'
        print(print_row)

def get_matrix_max_chars(matrix: list[list[int]]) -> int:
    max_chars: int = 1
    for row in matrix:
        length_arr: list[int] = [len(str(cell)) for cell in row]
        max_chars = max(length_arr) if max(length_arr) > max_chars else max_chars
    return max_chars

if '__main__' == __name__:
    main()