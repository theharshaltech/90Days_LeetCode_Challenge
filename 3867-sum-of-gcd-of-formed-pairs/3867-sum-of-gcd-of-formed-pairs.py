class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Construct prefixGcd
        prefixGcd = []
        mx = 0

        for num in nums:
            if num > mx:
                mx = num
            prefixGcd.append(gcd(num, mx))

        # Sort the array
        prefixGcd.sort()

        # Pair smallest with largest
        ans = 0
        left = 0
        right = len(prefixGcd) - 1

        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1

        return ans