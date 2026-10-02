class Solution(object):
    def generateParenthesis(self, n):
        ans = []

        def dfs(l, r, s):
            if l == 0 and r == 0:
                ans.append(''.join(s))
                return

            if l > 0:
                s.append('(')
                dfs(l - 1, r, s)
                s.pop()

            if l < r:
                s.append(')')
                dfs(l, r - 1, s)
                s.pop()

        dfs(n, n, [])
        return ans