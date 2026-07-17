class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        maxNum = max(nums)

        # Count frequency of every number
        freq = [0] * (maxNum + 1)
        for num in nums:
            freq[num] += 1

        # divisibleCount[i] = how many numbers are divisible by i
        divisibleCount = [0] * (maxNum + 1)

        for i in range(1, maxNum + 1):
            for j in range(i, maxNum + 1, i):
                divisibleCount[i] += freq[j]

        # gcdCount[i] = number of pairs having GCD exactly i
        gcdCount = [0] * (maxNum + 1)

        for i in range(maxNum, 0, -1):

            count = divisibleCount[i]

            # Total pairs divisible by i
            gcdCount[i] = count * (count - 1) // 2

            # Remove pairs already counted for larger multiples
            multiple = i * 2
            while multiple <= maxNum:
                gcdCount[i] -= gcdCount[multiple]
                multiple += i

        # Build prefix sum
        prefix = []
        gcdValue = []

        total = 0
        for i in range(1, maxNum + 1):
            if gcdCount[i] > 0:
                total += gcdCount[i]
                prefix.append(total)
                gcdValue.append(i)

        # Answer queries
        answer = []

        for q in queries:
            index = bisect_left(prefix, q + 1)
            answer.append(gcdValue[index])

        return answer