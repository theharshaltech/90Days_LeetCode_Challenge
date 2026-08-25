class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = set(nums)

        multiple = k

        while multiple in nums:
            multiple += k

        return multiple