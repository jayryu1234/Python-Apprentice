# Text Yourself
# In the comprehensions below, replace the ...
# with code that will produce the expected output.

board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

# Uncomment below and replace the ... with code that will produce the expected output.
dx1 = 0
dx2 = 0
d1 = []
for i in range(3):
    d1.append(board[dx1][dx2])
    dx1 += 1
    dx2 += 1
print(d1)
