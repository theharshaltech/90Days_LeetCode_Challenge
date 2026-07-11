class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in range(n)]

        # Build the graph
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = [False] * n
        answer = 0

        for i in range(n):
            if not visited[i]:
                # Find all vertices in this component
                stack = [i]
                visited[i] = True
                component = []

                while stack:
                    node = stack.pop()
                    component.append(node)

                    for neighbor in graph[node]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            stack.append(neighbor)

                # In a complete component of size k,
                # every vertex must have degree k - 1
                size = len(component)
                complete = True

                for node in component:
                    if len(graph[node]) != size - 1:
                        complete = False
                        break

                if complete:
                    answer += 1

        return answer