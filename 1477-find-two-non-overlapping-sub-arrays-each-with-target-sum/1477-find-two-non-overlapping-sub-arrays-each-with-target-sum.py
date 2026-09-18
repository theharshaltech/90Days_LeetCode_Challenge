class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        INF = float('inf')
        best = [INF] * n
        ans = INF
        
        left = 0
        curr = 0
        
        for right in range(n):
            curr += arr[right]
            
            while curr > target:
                curr -= arr[left]
                left += 1
                
            if right > 0:
                best[right] = best[right - 1]
                
            if curr == target:
                length = right - left + 1
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])
                best[right] = min(best[right], length)
                
        return ans if ans != INF else -1