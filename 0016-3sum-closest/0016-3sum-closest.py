class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        ans = sum(nums[:3])

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(total - target) < abs(ans - target):
                    ans = total

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total

        return ans