class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(s)

        prefix_sum = [0] * (n + 1)
        prefix_nonzero = [0] * (n + 1)

        digits = []

        for i, ch in enumerate(s):
            d = int(ch)
            prefix_sum[i + 1] = prefix_sum[i] + d
            prefix_nonzero[i + 1] = prefix_nonzero[i] + (d != 0)

            if d != 0:
                digits.append(d)

        prefix_num = [0] * (len(digits) + 1)

        for i in range(len(digits)):
            prefix_num[i + 1] = (prefix_num[i] * 10 + digits[i]) % MOD

        power10 = [1] * (len(digits) + 1)

        for i in range(1, len(digits) + 1):
            power10[i] = (power10[i - 1] * 10) % MOD

        answer = []

        for l, r in queries:
            digit_sum = prefix_sum[r + 1] - prefix_sum[l]

            left = prefix_nonzero[l]
            right = prefix_nonzero[r + 1] - 1

            if left > right:
                number = 0
            else:
                length = right - left + 1
                number = (prefix_num[right + 1] - prefix_num[left] * power10[length]) % MOD

            answer.append((number * digit_sum) % MOD)

        return answer