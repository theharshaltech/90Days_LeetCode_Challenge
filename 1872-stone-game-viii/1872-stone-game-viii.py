class Solution(object):
    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n = len(stones)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stones[i]

        dp = [0] * (n + 1)

        best = float('-inf')

        for i in range(n - 1, 0, -1):
            best = max(best, prefix[i + 1] - dp[i + 1])
            dp[i] = best

        return dp[1]