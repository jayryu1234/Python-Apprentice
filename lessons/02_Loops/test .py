def pretty_print_2d(a):
    "" "Prints a 2D array in a pretty way" ""
    for row in a:
        print(row)

board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

pretty_print_2d(board)
print()

transposed = list(zip(*board)) # <--- HERE IS THE MAGIC
pretty_print_2d(transposed)