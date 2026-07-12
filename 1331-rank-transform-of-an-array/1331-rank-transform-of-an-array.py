class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        sorted_arr = sorted(set(arr))
        rank = {}
        for i in range(len(sorted_arr)):
                rank[sorted_arr[i]] = i + 1
        ans = []
        for num in arr:
            ans.append(rank[num])
        return ans