class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        small = min(nums)
        large = max(nums)

        while large:
            small, large = large, small % large

        return small