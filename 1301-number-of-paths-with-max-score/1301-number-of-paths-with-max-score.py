class Solution(object):
    def pathsWithMaxScore(self, board):
        """
        :type board: List[str]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(board)

        # dp_score[i][j] = maximum score from (i,j) to S
        dp_score = [[-1] * n for _ in range(n)]

        # dp_count[i][j] = number of maximum-score paths
        dp_count = [[0] * n for _ in range(n)]

        dp_score[n - 1][n - 1] = 0
        dp_count[n - 1][n - 1] = 1

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):

                if board[i][j] == 'X':
                    continue

                if i == n - 1 and j == n - 1:
                    continue

                best = -1
                ways = 0

                # Down
                if i + 1 < n and dp_score[i + 1][j] != -1:
                    if dp_score[i + 1][j] > best:
                        best = dp_score[i + 1][j]
                        ways = dp_count[i + 1][j]
                    elif dp_score[i + 1][j] == best:
                        ways = (ways + dp_count[i + 1][j]) % MOD

                # Right
                if j + 1 < n and dp_score[i][j + 1] != -1:
                    if dp_score[i][j + 1] > best:
                        best = dp_score[i][j + 1]
                        ways = dp_count[i][j + 1]
                    elif dp_score[i][j + 1] == best:
                        ways = (ways + dp_count[i][j + 1]) % MOD

                # Diagonal
                if i + 1 < n and j + 1 < n and dp_score[i + 1][j + 1] != -1:
                    if dp_score[i + 1][j + 1] > best:
                        best = dp_score[i + 1][j + 1]
                        ways = dp_count[i + 1][j + 1]
                    elif dp_score[i + 1][j + 1] == best:
                        ways = (ways + dp_count[i + 1][j + 1]) % MOD

                if best == -1:
                    continue

                value = 0
                if board[i][j] not in "SE":
                    value = int(board[i][j])

                dp_score[i][j] = best + value
                dp_count[i][j] = ways

        if dp_score[0][0] == -1:
            return [0, 0]

        return [dp_score[0][0], dp_count[0][0]]