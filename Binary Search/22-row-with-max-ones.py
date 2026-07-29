# Find the row with maximum ones

# Given a m x n binary matrix mat, find the 0-indexed position of the row that contains the maximum count of ones, and the number of ones in that row.
# In case there are multiple rows that have the maximum count of ones, the row with the smallest row number should be selected.
# Return an array containing the index of the row, and the number of ones in it.

class Solution:

    # Brute ~ simplest , optimal if rows are unsorted
    def rowAndMaximumOnes(self, mat:list[list[int]]) -> list[int]:
        row = 0
        max_ones = 0

        for i in range(len(mat)):
            cnt = sum(mat[i])

            if cnt > max_ones:
                max_ones = cnt
                row = i

        return [row, max_ones]
    

    # Optimal ~ if rows of matrix are sorted
    def lower_bound(self, nums, x):
        n = len(nums)
        low, high = 0, n-1
        ans = n

        while low<=high:
            mid = (low + high) // 2
            if nums[mid] >= x:
                # may be an answer
                ans = mid
                # look on left for smallest index
                high = mid - 1

            else:
                low = mid + 1
        
        return ans

    def rowAndMaximumOnes2(self, mat:list[list[int]]) -> list[int]:
        m, n = len(mat), len(mat[0])
        max_ones, row = 0, 0

        for i in range(m):
            # Calculate count of 1s using lower bound
            cnt = n - self.lower_bound(sorted(mat[i]), 1)

            if cnt>max_ones:
                max_ones = cnt
                row = i

        return [row, max_ones]
    

if __name__ == "__main__":
    matrix = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]

    sol = Solution()
    res = sol.rowAndMaximumOnes(matrix)
    # res = sol.rowAndMaximumOnes2(matrix)

    print(res)