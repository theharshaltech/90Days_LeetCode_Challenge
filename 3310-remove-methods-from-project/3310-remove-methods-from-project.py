class Solution(object):
    def remainingMethods(self, n, k, invocations):
        """
        :type n: int
        :type k: int
        :type invocations: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)

        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            u = stack.pop()
            for v in graph[u]:
                if not suspicious[v]:
                    suspicious[v] = True
                    stack.append(v)

        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))

        ans = []
        for i in range(n):
            if not suspicious[i]:
                ans.append(i)

        return ans