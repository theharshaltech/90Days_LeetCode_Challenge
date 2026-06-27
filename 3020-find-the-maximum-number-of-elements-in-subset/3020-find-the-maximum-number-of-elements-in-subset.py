from collections import Counter

class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Renamed 'count' to 'freq' to avoid the LeetCode environment conflict
        freq = Counter(nums)
        max_len = 0
        
        # 1. Handle the special case for base '1'
        if 1 in freq:
            c = freq[1]
            max_len = c if c % 2 != 0 else c - 1
            
        # 2. Process all other numbers as potential bases
        for x in freq:
            if x == 1:
                continue
                
            current_len = 0
            curr = x
            
            # Chain upward while we have pairs to place on both sides
            while freq[curr] >= 2:
                current_len += 2
                curr = curr * curr
                
            # If the next value exists at least once, it can cap our peak
            if freq[curr] >= 1:
                current_len += 1
            else:
                # If it doesn't exist, the last processed number becomes the peak
                current_len -= 1
                
            max_len = max(max_len, current_len)
            
        return max_len