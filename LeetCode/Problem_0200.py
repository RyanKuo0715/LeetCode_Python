# LeetCode Problem 200: Number of Islands
# https://leetcode.com/problems/number-of-islands/description/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '1':
                    self.find_island(grid, y, x)
                    count += 1
        return count

    def find_island(self, grid, y, x):
        if grid[y][x] == '1':
            grid[y][x] = '0'
            for y_temp in [max(0, y - 1), min(y + 1, len(grid) - 1)]:
                self.find_island(grid, y_temp, x)
            for x_temp in [max(0, x - 1), min(x + 1, len(grid[y]) - 1)]:
                self.find_island(grid, y, x_temp)
