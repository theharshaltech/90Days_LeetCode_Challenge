class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = sorted(nums1 + nums2)
        n = len(nums)

        mid = n // 2

        if n % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2.0

        return float(nums[mid])