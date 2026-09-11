class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        count = 0

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            a = num // 100
            b = (num // 10) % 10
            c = num % 10

            temp = digits[:]

            possible = True

            for d in [a, b, c]:
                if d in temp:
                    temp.remove(d)
                else:
                    possible = False
                    break

            if possible:
                count += 1

        return count