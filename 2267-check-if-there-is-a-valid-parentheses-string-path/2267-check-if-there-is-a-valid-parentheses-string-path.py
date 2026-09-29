class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])

        if (m + n - 1) % 2 != 0:
            return False

        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                change = 1 if grid[i][j] == '(' else -1

                if i > 0:
                    for balance in dp[i - 1][j]:
                        if balance + change >= 0:
                            dp[i][j].add(balance + change)

                if j > 0:
                    for balance in dp[i][j - 1]:
                        if balance + change >= 0:
                            dp[i][j].add(balance + change)

        return 0 in dp[m - 1][n - 1]