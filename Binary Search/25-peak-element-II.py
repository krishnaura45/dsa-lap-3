# Peak Element in 2D matrix
# It's an element that is strictly greater than its neighbors - above, before, after, below it.

# Find Indices of any peak element in 2D array (Variation ~ list of peaks in matrix)
class Solution:
    # Brute ~ Scan through every element and find out peak
    def findPeak2D(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
               if (i==0 or mat[i][j]>mat[i-1][j]) and (j==0 or mat[i][j]>mat[i][j-1]) and (i==m-1 or mat[i][j]>mat[i+1][j]) and (j==n-1 or mat[i][j]>mat[i][j+1]):
                   return [i,j]
               
        return [-1,-1]
    
    # Slight Better at time ~ Find the largest element in the matrix as it'll definitely be a peak element
    def findPeak2D_sb(self, mat: list[list[int]]) -> int:
            m, n = len(mat), len(mat[0])
            largest = -1
            peak_row, peak_col = -1, -1

            for i in range(m):
                for j in range(n):
                   if mat[i][j]>largest:
                       peak_row, peak_col = i, j
                       largest = mat[i][j]
                   
            return [peak_row, peak_col]

    
    # Optimal ~ BS
    def maxElRow(self, mat, col):
        ans = -1
        maxi = -1
        for i in range(len(mat)):
            if mat[i][col]>maxi:
                maxi = mat[i][col]
                ans = i

        return ans

    def findPeak2D_op(self, mat: list[list[int]]) -> int:
        m, n = len(mat), len(mat[0])
        low, high = 0, n-1

        while low<=high:
            mid = (low + high)//2

            row = self.maxElRow(mat, mid)
            left = mat[row][mid-1] if mid-1>=0 else -1
            right = mat[row][mid+1] if mid+1<n else -1

            if mat[row][mid]>left and mat[row][mid]>right:
                return [row,mid]

            elif mat[row][mid]<left:
                high = mid - 1

            else:
                low = mid + 1

        return [-1,-1]


if __name__=="__main__":
    # matrix = list[list(map(int, input().split()))]
    matrix = [[1,2,3,4,5],[6,7,8,9,10]]

    sol = Solution()
    # print(f"Peak Element Index: {sol.findPeak2D(matrix)}")
    # print(f"Peak Element Index: {sol.findPeak2D_sb(matrix)}")
    print(f"Peak Element Index: {sol.findPeak2D_op(matrix)}")