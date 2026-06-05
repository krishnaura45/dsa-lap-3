# Set Matrix Zeroes (Medium)
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

class Solution:

    # helpers for brute force
    def markRow(self, arr: list[list[int]], i:int) -> None:
        n = len(arr[0])
        # iterate over columns
        for j in range(n):
            if arr[i][j]!=0:
                arr[i][j] = float('inf')

    def markColumn(self, arr: list[list[int]], j:int) -> None:
        m = len(arr)
        # Iterate over rows
        for i in range(m):
            if arr[i][j]!=0:
                arr[i][j] = float('inf')

    # brute
    def setMatZeroes(self, arr:list[list[int]]):
        m = len(arr)           # rows
        n = len(arr[0])        # columns

        for i in range(m):
            for j in range(n):
                if arr[i][j]==0:
                    self.markRow(arr,i)
                    self.markColumn(arr,j)

        for i in range(m):
            for j in range(n):
                if arr[i][j]==float('inf'):
                    arr[i][j] = 0

        return arr
    # TC ~ O(nm*(n+m)) --> O(n^3), SC ~ O(1)
    
    # better
    def setMatZeroes2(self, arr:list[list[int]]):
        m = len(arr)
        n = len(arr[0])

        # to keep track of rows/columns that will be 0's at end
        rowt = [0]*m
        colt = [0]*n

        for i in range(m):
            for j in range(n):
                if arr[i][j]==0:
                    rowt[i] = 1
                    colt[j] = 1

        for i in range(m):
            for j in range(n):
                if rowt[i]==1 or colt[j]==1:
                    arr[i][j] = 0

        return arr
    # TC ~ O(2mn), SC ~ O(n+m)

    # optimal
    def setMatZeroes3(self, arr:list[list[int]]):
        m = len(arr)
        n = len(arr[0])

        # No need to separately define tracker arrays
        # rowt --> arr[..][0]   // row tracker
        # colt --> arr[0][..]   // column tracker

        # First Traversal
        col0 = 1
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 0:
                    # mark i-th row
                    arr[i][0] = 0

                    # mark j-th column
                    if j!=0:
                        arr[0][j] = 0
                    else:
                        col0 = 0

        # Second Traversal ~ Mark with 0 from (1,1) to (m-1, n-1)
        for i in range(m-1, -1, -1):
            for j in range(n-1, 0, -1):
                if arr[i][j] != 0:       # optional
                    if arr[i][0] == 0 or arr[0][j] == 0:
                        arr[i][j] = 0

        # Update first row then first column
        if arr[0][0] == 0:
            for j in range(n):
                arr[0][j] = 0

        if col0 == 0:
            for i in range(m):
                arr[i][0] = 0

        return arr
    # TC ~ O(2mn + m + n) --> O(mn), SC ~ O(1)

if __name__=="__main__":
    arr = [[2,1,1,5],[1,0,0,1],[1,1,0,1],[4,1,1,3]]
    arr2 = [[1,1,1,1],[1,0,1,1],[1,1,0,1],[0,1,1,1]]

    sol = Solution()

    res = sol.setMatZeroes(arr)
    # res = sol.setMatZeroes2(arr)
    res2 = sol.setMatZeroes3(arr2)

    for row in res:
        print(row)

    print()
    for row in res2:
        print(row)