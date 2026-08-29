class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """
        n = len(nums)

        arr = sorted((value, index) for index, value in enumerate(nums))

        groups = []
        current = [arr[0]]

        for i in range(1, n):
            if arr[i][0] - arr[i - 1][0] <= limit:
                current.append(arr[i])
            else:
                groups.append(current)
                current = [arr[i]]

        groups.append(current)

        ans = nums[:]

        for group in groups:
            values = sorted(value for value, index in group)
            indices = sorted(index for value, index in group)

            for index, value in zip(indices, values):
                ans[index] = value

        return ans