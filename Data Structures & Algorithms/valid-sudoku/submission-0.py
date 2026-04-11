class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		rowSet = defaultdict(list)
		colSet = defaultdict(list)
		boxSet = defaultdict(list)

		for r in range(len(board)):
			for c in range(len(board[r])):
				if board[r][c] == '.':
					continue
					 
				if board[r][c] in rowSet[r]:
					return False

				if board[r][c] in colSet[c]:
					return False

				if board[r][c] in boxSet[(r//3)*3 + (c//3)]:
					return False

				rowSet[r].append(board[r][c])
				colSet[c].append(board[r][c])
				boxSet[(r//3)*3 + (c//3)].append(board[r][c])
			
		return True