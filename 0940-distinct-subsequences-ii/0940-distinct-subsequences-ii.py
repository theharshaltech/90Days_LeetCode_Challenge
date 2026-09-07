class Solution(object):
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """
        MOD = 10**9 + 7
        
        dp = [0] * 26
        
        for ch in s:
            i = ord(ch) - ord('a')
            total = sum(dp) + 1
            dp[i] = total % MOD
        
        return sum(dp) % MOD