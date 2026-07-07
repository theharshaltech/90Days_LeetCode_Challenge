class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        digit_sum = 0

        for digit in str(n):
            if digit != '0':
                num = int(digit)
                x = x * 10 + num
                digit_sum = digit_sum + num

        return x * digit_sum