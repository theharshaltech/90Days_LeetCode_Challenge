class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for i in range(len(target) - 1, -1, -1):
            temp = count[:]
            possible = True

            for j in range(i):
                x = ord(target[j]) - ord('a')

                if temp[x] == 0:
                    possible = False
                    break

                temp[x] -= 1

            if not possible:
                continue

            t = ord(target[i]) - ord('a')

            for c in range(t + 1, 26):
                if temp[c] > 0:
                    temp[c] -= 1
                    result = target[:i] + chr(c + ord('a'))

                    for x in range(26):
                        result += chr(x + ord('a')) * temp[x]

                    return result

        return ""