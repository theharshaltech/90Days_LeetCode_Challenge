class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs',
            '8': 'tuv', '9': 'wxyz'
        }

        ans = [""]

        for digit in digits:
            ans = [
                prefix + char
                for prefix in ans
                for char in phone[digit]
            ]

        return ans