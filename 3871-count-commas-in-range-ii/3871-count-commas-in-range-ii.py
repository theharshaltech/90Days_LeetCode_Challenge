class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        power = 1000
        commas = 1

        while power <= n:
            total += n - power + 1
            power *= 1000
            commas += 1

        return total