class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)

        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        arr.sort()

        starts = [x[0] for x in arr]

        nxt = [0] * n
        for i in range(n):
            nxt[i] = bisect_right(starts, arr[i][1])

        memo = {}

        def dp(i, k):
            if i >= n or k == 0:
                return (0, ())

            if (i, k) in memo:
                return memo[(i, k)]

            score1, indices1 = dp(i + 1, k)

            score2, indices2 = dp(nxt[i], k - 1)
            score2 += arr[i][2]

            current = tuple(sorted(indices2 + (arr[i][3],)))

            if score2 > score1:
                ans = (score2, current)
            elif score2 < score1:
                ans = (score1, indices1)
            else:
                ans = (score1, min(indices1, current))

            memo[(i, k)] = ans
            return ans

        score, answer = dp(0, 4)

        return list(answer)