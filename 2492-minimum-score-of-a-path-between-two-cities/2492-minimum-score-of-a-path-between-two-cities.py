class Solution(object):
    def minScore(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)

        for u, v, d in roads:
            graph[u].append((v, d))
            graph[v].append((u, d))

        visited = set()
        ans = [float('inf')]

        def dfs(node):
            visited.add(node)

            for nei, dist in graph[node]:
                ans[0] = min(ans[0], dist)
                if nei not in visited:
                    dfs(nei)

        dfs(1)
        return ans[0]