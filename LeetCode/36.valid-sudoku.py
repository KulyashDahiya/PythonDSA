#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue

                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])

                if board[i][j] in columns[j]:
                    return False
                columns[j].add(board[i][j])

                box_index = (i // 3) * 3 + (j//3)

                if board[i][j] in boxes[box_index]:
                    return False
                boxes[box_index].add(board[i][j])

        return True

        
# @lc code=end

