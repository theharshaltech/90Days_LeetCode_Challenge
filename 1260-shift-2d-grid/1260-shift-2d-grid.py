class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])

        # Convert 2D grid to 1D list
        arr = []
        for row in grid:
            arr.extend(row)

        # Shift the array
        k = k % (m * n)
        arr = arr[-k:] + arr[:-k]

        # Convert back to 2D grid
        ans = []
        index = 0

        for i in range(m):
            row = []
            for j in range(n):
                row.append(arr[index])
                index += 1
            ans.append(row)

        return ans