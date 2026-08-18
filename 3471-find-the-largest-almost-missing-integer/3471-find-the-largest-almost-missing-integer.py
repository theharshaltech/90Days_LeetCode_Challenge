class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        count = [0] * 51

        # Check every subarray of size k
        for i in range(n - k + 1):
            seen = set()

            for j in range(i, i + k):
                seen.add(nums[j])

            for x in seen:
                count[x] += 1

        # Find the largest number appearing in exactly one subarray
        ans = -1

        for x in range(51):
            if count[x] == 1:
                ans = x

        return ans