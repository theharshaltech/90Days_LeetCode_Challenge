class Solution(object):
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        """
        :type n: int
        :type nums: List[int]
        :type maxDiff: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        arr = sorted((nums[i], i) for i in range(n))

        values = [x[0] for x in arr]

        # position of original index in sorted order
        pos = [0] * n
        for i in range(n):
            pos[arr[i][1]] = i

        # Connected components
        comp = [0] * n
        cid = 0
        for i in range(1, n):
            if values[i] - values[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        # farthest reachable in one edge
        nxt = [0] * n
        r = 0
        for i in range(n):
            while r + 1 < n and values[r + 1] - values[i] <= maxDiff:
                r += 1
            nxt[i] = r

        # Binary lifting
        LOG = max(1, n.bit_length())
        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []

        for u, v in queries:
            a = pos[u]
            b = pos[v]

            if a == b:
                ans.append(0)
                continue

            if comp[a] != comp[b]:
                ans.append(-1)
                continue

            if a > b:
                a, b = b, a

            steps = 0
            cur = a

            for k in range(LOG - 1, -1, -1):
                nxt_pos = up[k][cur]
                if nxt_pos < b:
                    steps += 1 << k
                    cur = nxt_pos

            ans.append(steps + 1)

        return ans
        