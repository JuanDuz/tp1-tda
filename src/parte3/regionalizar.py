def is_initial_quadrant(quadrant):
    return quadrant == -1


def divide_in_regions(board, n, silo_row, silo_col, initial_row, initial_col, region=1, actual_quadrant=-1, silo_quadrant=-1):
    # Step 1: Check base case. Sets the three cells in L shape as a new region
    if n == 2:
        for i in range(2):
            for j in range(2):
                if board[initial_row + i][initial_col + j] == 0:
                    board[initial_row + i][initial_col + j] = region
        return region + 1

    # Step 2: Identify correct L angle and fill with fake silos
    middle = n // 2

    if is_initial_quadrant(actual_quadrant):
        silo_quadrant = (2 if silo_row >= initial_row + middle else 0) + (1 if silo_col >= initial_col + middle else 0)
        fill_fake_silos_in_L_shape_pointing_real_silo(board, middle, initial_row, initial_col, silo_quadrant)
    elif actual_quadrant == silo_quadrant:
        subquadrant_silo = (2 if silo_row >= initial_row + middle else 0) + (1 if silo_col >= initial_col + middle else 0)
        fill_fake_silos_in_L_shape_pointing_real_silo(board, middle, initial_row, initial_col, subquadrant_silo)
    else:
        fill_fake_silos_in_L_shape_pointing_center(board, middle, initial_row, initial_col, actual_quadrant)
    silo_quadrant = (2 if silo_row >= initial_row + middle else 0) + (1 if silo_col >= initial_col + middle else 0)

    # Step 3: Divide in suproblems and resolve them recursively
    new_region = region

    # Quadrant 0
    new_region = divide_in_regions(board, middle, silo_row, silo_col, initial_row, initial_col,
                                     new_region, 0, silo_quadrant)

    # Quadrant 1
    new_region = divide_in_regions(board, middle, silo_row, silo_col, initial_row, initial_col + middle,
                                     new_region, 1, silo_quadrant)
    # Quadrant 2
    new_region = divide_in_regions(board, middle, silo_row, silo_col, initial_row + middle, initial_col,
                                     new_region, 2, silo_quadrant)
    # Quadrant 3
    new_region = divide_in_regions(board, middle, silo_row, silo_col, initial_row + middle, initial_col + middle,
                                     new_region, 3, silo_quadrant)

    # Step 4: Once all 4 subproblem were conquered, fill the fake silos (which were filled in step 2) as a new region
    for i in range(initial_row + middle - 1, initial_row + middle + 1):
        for j in range(initial_col + middle - 1, initial_col + middle + 1):
            if board[i][j] == -2:
                board[i][j] = new_region
    print_board(board)
    return new_region + 1


def fill_fake_silos_in_L_shape_pointing_real_silo(board, middle, initial_row, initial_col, quadrant):
    if quadrant == 0:
        board[initial_row + middle - 1][initial_col + middle] = -2
        board[initial_row + middle][initial_col + middle - 1] = -2
        board[initial_row + middle][initial_col + middle] = -2
    elif quadrant == 1:
        board[initial_row + middle - 1][initial_col + middle - 1] = -2
        board[initial_row + middle][initial_col + middle] = -2
        board[initial_row + middle][initial_col + middle - 1] = -2
    elif quadrant == 2:
        board[initial_row + middle - 1][initial_col + middle - 1] = -2
        board[initial_row + middle - 1][initial_col + middle] = -2
        board[initial_row + middle][initial_col + middle] = -2
    elif quadrant == 3:
        board[initial_row + middle - 1][initial_col + middle - 1] = -2
        board[initial_row + middle][initial_col + middle - 1] = -2
        board[initial_row + middle - 1][initial_col + middle] = -2


def fill_fake_silos_in_L_shape_pointing_center(board, middle, initial_row, initial_col, quadrant):
    if quadrant == 0:
        board[initial_row + middle - 1][initial_col + middle - 1] = -2
        board[initial_row + middle][initial_col + middle - 1] = -2
        board[initial_row + middle - 1][initial_col + middle] = -2
    elif quadrant == 1:
        board[initial_row + middle - 1][initial_col + middle - 1] = -2
        board[initial_row + middle - 1][initial_col + middle] = -2
        board[initial_row + middle][initial_col + middle] = -2
    elif quadrant == 2:
        board[initial_row + middle - 1][initial_col + middle - 1] = -2
        board[initial_row + middle][initial_col + middle] = -2
        board[initial_row + middle][initial_col + middle - 1] = -2
    elif quadrant == 3:
        board[initial_row + middle - 1][initial_col + middle] = -2
        board[initial_row + middle][initial_col + middle - 1] = -2
        board[initial_row + middle][initial_col + middle] = -2


def print_board(board):
    for fila in board:
        print(' '.join(str(x) if x != 0 else '-' for x in fila))


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("Uso: python regionalizar.py n silo_row silo_col")
        sys.exit()

    n = int(sys.argv[1])
    silo_row = int(sys.argv[2])
    silo_col = int(sys.argv[3])

    board = [[0 for _ in range(n)] for _ in range(n)]
    board[silo_row][silo_col] = -1
    divide_in_regions(board, n, silo_row, silo_col, 0, 0)
    print_board(board)
