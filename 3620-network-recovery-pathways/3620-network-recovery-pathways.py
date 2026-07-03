class Solution(object):
    def findMaxPathScore(self, edges, online, k):
        """
        :type edges: List[List[int]]
        :type online: List[bool]
        :type k: int
        :rtype: int
        """
        n = len(online)

        # Build graph and indegree
        graph = [[] for _ in range(n)]
        indegree = [0] * n
        edge_costs = []

        for u, v, cost in edges:
            graph[u].append((v, cost))
            indegree[v] += 1
            edge_costs.append(cost)

        # Topological Sort
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)

            for nxt, cost in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        edge_costs = sorted(set(edge_costs))

        # Check if a path exists with minimum edge >= limit
        def check(limit):
            INF = float("inf")
            dist = [INF] * n
            dist[0] = 0

            for node in topo:
                if dist[node] == INF:
                    continue

                # Skip offline intermediate nodes
                if node != 0 and node != n - 1 and not online[node]:
                    continue

                for nxt, cost in graph[node]:

                    # Edge cost must be at least limit
                    if cost < limit:
                        continue

                    # Next node cannot be offline
                    if nxt != 0 and nxt != n - 1 and not online[nxt]:
                        continue

                    dist[nxt] = min(dist[nxt], dist[node] + cost)

            return dist[n - 1] <= k

        # Binary Search
        left = 0
        right = len(edge_costs) - 1
        answer = -1

        while left <= right:
            mid = (left + right) // 2

            if check(edge_costs[mid]):
                answer = edge_costs[mid]
                left = mid + 1
            else:
                right = mid - 1

        return answer