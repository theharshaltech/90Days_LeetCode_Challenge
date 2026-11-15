class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != pairs[ch]:
                    return False

        return len(stack) == 0