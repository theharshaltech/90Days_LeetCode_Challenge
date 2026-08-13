class Solution(object):
    def longestRepeating(self, s, queryCharacters, queryIndices):
        """
        :type s: str
        :type queryCharacters: str
        :type queryIndices: List[int]
        :rtype: List[int]
        """
        n = len(s)

        tree = [[None, None, 0, 0, 0, 0] for _ in range(4 * n)]

        def merge(a, b):
            leftChar = a[0]
            rightChar = b[1]

            leftLen = a[2]
            rightLen = b[3]

            best = max(a[4], b[4])

            if a[1] == b[0]:

                best = max(best, a[3] + b[2])

                if a[2] == a[5]:
                    leftLen = a[5] + b[2]

                if b[3] == b[5]:
                    rightLen = a[3] + b[5]

            length = a[5] + b[5]

            return [
                leftChar,
                rightChar,
                leftLen,
                rightLen,
                best,
                length
            ]

        def build(node, left, right):
            if left == right:
                c = s[left]
                tree[node] = [c, c, 1, 1, 1, 1]
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, left, right, index, char):
            if left == right:
                tree[node] = [char, char, 1, 1, 1, 1]
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, right, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        answer = []

        for i in range(len(queryCharacters)):
            index = queryIndices[i]
            char = queryCharacters[i]

            update(1, 0, n - 1, index, char)

            answer.append(tree[1][4])

        return answer