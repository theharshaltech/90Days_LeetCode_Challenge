class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        rows = {}

        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        answer = 2 * n

        for seats in rows.values():
            left = 2 not in seats and 3 not in seats and 4 not in seats and 5 not in seats
            right = 6 not in seats and 7 not in seats and 8 not in seats and 9 not in seats
            middle = 4 not in seats and 5 not in seats and 6 not in seats and 7 not in seats

            if left and right:
                continue
            elif left or right or middle:
                answer -= 1
            else:
                answer -= 2

        return answer        