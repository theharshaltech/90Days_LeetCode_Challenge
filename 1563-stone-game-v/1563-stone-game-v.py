class Solution(object):
    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """
        n = len(stoneValue)

        s = [0] * (n + 1)

        for i in range(1, n + 1):
            s[i] = s[i - 1] + stoneValue[i - 1]

        f = [[0] * n for _ in range(n)]

        def dfs(i, j):
            if i == j:
                return 0

            if f[i][j]:
                return f[i][j]

            ans = 0
            a = 0

            for k in range(i, j):
                a += stoneValue[k]
                b = s[j + 1] - s[i] - a

                if a < b:
                    if ans >= a * 2:
                        continue

                    ans = max(ans, a + dfs(i, k))

                elif a > b:
                    if ans >= b * 2:
                        break

                    ans = max(ans, b + dfs(k + 1, j))

                else:
                    ans = max(ans, a + dfs(i, k), b + dfs(k + 1, j))

            f[i][j] = ans
            return ans

        return dfs(0, n - 1)