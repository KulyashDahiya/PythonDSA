#
# @lc app=leetcode id=2352 lang=python3
#
# [2352] Equal Row and Column Pairs
#

# @lc code=start
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        transpose = Counter(zip(*grid))
        grid = Counter(map(tuple, grid))

        return sum(transpose[t] * grid[t] for t in transpose)


        #     OR

        # n = len(grid)
        # column_grid = []

        # j = 0
        # while j < n:
        #     temp = []
        #     i = 0
        #     while i < n:
        #         temp.append(grid[i][j])
        #         i += 1
        #     j += 1
        #     column_grid.append(temp)

        # print(column_grid)
        # print(grid)
        # count = 0
        # for column in column_grid:
        #     for row in grid:
        #         if row == column:
        #             count += 1

        # return count


        
# @lc code=end

