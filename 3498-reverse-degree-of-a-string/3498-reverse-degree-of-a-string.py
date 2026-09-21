class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        for i in range(len(s)):
            reverse_value = ord('z') - ord(s[i]) + 1

            total += reverse_value * (i + 1)

        return total