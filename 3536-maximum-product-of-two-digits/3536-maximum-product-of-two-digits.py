class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = []

        while n > 0:
            digits.append(n % 10)
            n //= 10

        digits.sort(reverse=True)
        return digits[0] * digits[1]