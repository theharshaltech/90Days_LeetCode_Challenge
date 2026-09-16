class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        MOD = 1000000007
        
        dp = [[0] * n for _ in range(k + 1)]
        
        for j in range(n):
            dp[0][j] = 1
        
        for i in range(1, k + 1):
            total = 0
            
            for j in range(1, n):
                total += dp[i - 1][j - 1]
                total %= MOD
                
                dp[i][j] = dp[i][j - 1] + total
                dp[i][j] %= MOD
        
        return dp[k][n - 1]