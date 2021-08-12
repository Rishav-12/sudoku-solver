board = [[5, 0, 0, 2, 0, 0, 0, 4, 0],
	[0, 0, 0, 6, 0, 3, 0, 0, 0],
	[0, 3, 0, 0, 0, 9, 0, 0, 7],
	[0, 0, 3, 0, 0, 7, 0, 0, 0],
	[0, 0, 7, 0, 0, 8, 0, 0, 0],
	[6, 0, 0, 0, 0, 0, 0, 2, 0],
	[0, 8, 0, 0, 0, 0, 0, 0, 3],
	[0, 0, 0, 4, 0, 0, 6, 0, 0],
	[0, 0, 0, 1, 0, 0, 5, 0, 0]]


def print_board(board):
	for i in range(len(board)):
		if i % 3 == 0 and i != 0:
			print("- - - - - - - - - - - - -")
		for j in range(len(board[0])):
			if j % 3 == 0 and j != 0:
				print(" | ", end = "")

			if j == 8:
				print(board[i][j])
			else:
				print(str(board[i][j]) + " ", end = "")

def find_empty_cell(board):
	for i in range(9):
		for j in range(9):
			if board[i][j] == 0:
				return (i, j)

def possible(board, row, col, num):

	# Check column
	for i in range(9):
		if board[i][col] == num:
			return False

	# Check row
	for i in range(9):
		if board[row][i] == num:
			return False
	
	# Check 3x3 square
	istart = (row // 3) * 3
	jstart = (col // 3) * 3

	for i in range(istart, istart + 3):
		for j in range(jstart, jstart + 3):
			if board[i][j] == num:
				return False
	return True

def solve(board):
	pos = find_empty_cell(board)

	if not pos:
		return True
	else:
		i, j = pos

	for num in range(1, 10):
		if possible(board, i, j, num):
			board[i][j] = num

			if solve(board):
				return True

			board[i][j] = 0

	return False

print_board(board)
solve(board)
print("\n\n")
print_board(board)
