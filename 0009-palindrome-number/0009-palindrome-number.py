class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        original = x
        rev = 0
        n = x

        while n > 0:
            digit = n % 10
            rev = rev * 10 + digit
            n = n // 10

        return original == rev