import unittest
from src.parte3.regionalizar import divide_in_regions


class TestRegionalizar(unittest.TestCase):

    """"""""""""
    """ n = 8 """
    """"""""""""

    def test_regionalize_n_equals_eight_silo_at_center(self):
        # Arrange
        n = 8
        board = [[0 for _ in range(n)] for _ in range(n)]
        silo_row = 4
        silo_col = 4
        board[silo_row][silo_col] = -1


        expected_board = [
            [1, 1, 2, 2, 6, 6, 7, 7],
            [1, 5, 5, 2, 6, 10, 10, 7],
            [3, 5, 4, 4, 8, 8, 10, 9],
            [3, 3, 4, 21, 21, 8, 9, 9],
            [11, 11, 12, 21, -1, 16, 17, 17],
            [11, 15, 12, 12, 16, 16, 20, 17],
            [13, 15, 15, 14, 18, 20, 20, 19],
            [13, 13, 14, 14, 18, 18, 19, 19]
        ]

        # Act
        divide_in_regions(board, n, silo_row, silo_col, 0, 0)

        # Assert
        self.assertEqual(expected_board, board)

    def test_regionalize_n_equals_eight_silo_next_to_center(self):
        # Arrange
        n = 8
        board = [[0 for _ in range(n)] for _ in range(n)]
        silo_row = 5
        silo_col = 5
        board[silo_row][silo_col] = -1

        expected_board = [
            [1,   1,  2,  2,  6,  6,  7,  7],
            [1,   5,  5,  2,  6, 10, 10,  7],
            [3,   5,  4,  4,  8,  8, 10,  9],
            [3,   3,  4, 21,  21,  8,  9,  9],
            [11, 11, 12, 21, 16, 16, 17, 17],
            [11, 15, 12, 12, 16, -1, 20, 17],
            [13, 15, 15, 14, 18, 20, 20, 19],
            [13, 13, 14, 14, 18, 18, 19, 19]
        ]

        # Act
        divide_in_regions(board, n, silo_row, silo_col, 0, 0)

        # Assert
        self.assertEqual(expected_board, board)

    def test_regionalize_n_equals_eight_silo_at_edge(self):
        # Arrange
        n = 8
        board = [[0 for _ in range(n)] for _ in range(n)]
        silo_row = 7
        silo_col = 7
        board[silo_row][silo_col] = -1

        expected_board = [
            [1,   1,  2,  2,  6,  6,  7,  7],
            [1,   5,  5,  2,  6, 10, 10,  7],
            [3,   5,  4,  4,  8,  8, 10,  9],
            [3,   3,  4, 21, 21,  8,  9,  9],
            [11, 11, 12, 21, 16, 16, 17, 17],
            [11, 15, 12, 12, 16, 20, 20, 17],
            [13, 15, 15, 14, 18, 20, 19, 19],
            [13, 13, 14, 14, 18, 18, 19, -1]
        ]

        # Act
        divide_in_regions(board, n, silo_row, silo_col, 0, 0, 1)

        # Assert
        self.assertEqual(board, expected_board)

    def test_regionalize_n_equals_eight_silo_at_center_edge(self):
        # Arrange
        n = 8
        board = [[0 for _ in range(n)] for _ in range(n)]
        silo_row = 0
        silo_col = 4
        board[silo_row][silo_col] = -1

        expected_board = [
            [1,  1,   2,  2, -1, 6,  7,   7],
            [1,  5,   5,  2,  6,  6, 10,  7],
            [3,  5,   4,  4,  8, 10, 10,  9],
            [3,  3,   4, 21,  8,  8,  9,  9],
            [11, 11, 12, 21, 21, 16, 17, 17],
            [11, 15, 12, 12, 16, 16, 20, 17],
            [13, 15, 15, 14, 18, 20, 20, 19],
            [13, 13, 14, 14, 18, 18, 19, 19]
        ]

        # Act
        divide_in_regions(board, n, silo_row, silo_col, 0, 0, 1)

        # Assert
        self.assertEqual(expected_board, board)

    """"""""""""
    """ n = 4 """
    """"""""""""

    def test_regionalize_n_equals_four_silo_at_one_one(self):
        # Arrange
        n = 4
        board = [[0 for _ in range(n)] for _ in range(n)]
        silo_row = 1
        silo_col = 1
        board[silo_row][silo_col] = -1

        expected_board = [
            [1,  1, 2, 2],
            [1, -1, 5, 2],
            [3,  5, 5, 4],
            [3,  3, 4, 4]
        ]

        # Act
        divide_in_regions(board, n, silo_row, silo_col, 0, 0, 1)

        # Assert
        self.assertEqual(expected_board, board)

    def test_regionalize_n_equals_four_silo_at_two_two(self):
        # Arrange
        n = 4
        board = [[0 for _ in range(n)] for _ in range(n)]
        silo_row = 2
        silo_col = 2
        board[silo_row][silo_col] = -1

        expected_board = [
            [1, 1,  2, 2],
            [1, 5,  5, 2],
            [3, 5, -1, 4],
            [3, 3,  4, 4]
        ]

        # Act
        divide_in_regions(board, n, silo_row, silo_col, 0, 0, 1)

        # Assert
        self.assertEqual(expected_board, board)

    def test_regionalize_n_equals_four_silo_at_zero_three(self):
        # Arrange
        n = 4
        board = [[0 for _ in range(n)] for _ in range(n)]
        silo_row = 0
        silo_col = 3
        board[silo_row][silo_col] = -1

        expected_board = [
            [1, 1, 2, -1],
            [1, 5, 2, 2],
            [3, 5, 5, 4],
            [3, 3, 4, 4]
        ]

        # Act
        divide_in_regions(board, n, silo_row, silo_col, 0, 0, 1)

        # Assert
        self.assertEqual(expected_board, board)

    """"""""""""
    """ n = 2 """
    """"""""""""

    def test_regionalize_n_equals_two_silo_at_zero_zero(self):
        # Arrange
        n = 2
        board = [[0 for _ in range(n)] for _ in range(n)]
        silo_row = 0
        silo_col = 0
        board[silo_row][silo_col] = -1

        expected_board = [
            [-1, 1],
            [1, 1]
        ]

        # Act
        divide_in_regions(board, n, silo_row, silo_col, 0, 0, 1)

        # Assert
        self.assertEqual(expected_board, board)

    def test_regionalize_n_equals_two_silo_at_zero_one(self):
        # Arrange
        n = 2
        board = [[0 for _ in range(n)] for _ in range(n)]
        silo_row = 0
        silo_col = 1
        board[silo_row][silo_col] = -1

        expected_board = [
            [1, -1],
            [1, 1]
        ]

        # Act
        divide_in_regions(board, n, silo_row, silo_col, 0, 0, 1)

        # Assert
        self.assertEqual(expected_board, board)

    def test_regionalize_n_equals_two_silo_at_one_zero(self):
        # Arrange
        n = 2
        board = [[0 for _ in range(n)] for _ in range(n)]
        silo_row = 1
        silo_col = 0
        board[silo_row][silo_col] = -1

        expected_board = [
            [1, 1],
            [-1, 1]
        ]

        # Act
        divide_in_regions(board, n, silo_row, silo_col, 0, 0, 1)

        # Assert
        self.assertEqual(expected_board, board)

    def test_regionalize_n_equals_two_silo_at_one_one(self):
        # Arrange
        n = 2
        board = [[0 for _ in range(n)] for _ in range(n)]
        silo_row = 1
        silo_col = 1
        board[silo_row][silo_col] = -1

        expected_board = [
            [1, 1],
            [1, -1]
        ]

        # Act
        divide_in_regions(board, n, silo_row, silo_col, 0, 0, 1)

        # Assert
        self.assertEqual(expected_board, board)

if __name__ == '__main__':
    unittest.main()