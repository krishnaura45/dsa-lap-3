# Problem:
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

class Solution:

    # Brute ~ simplest naive
    def searchMatrix(self, mat: list[list[int]], target: int) -> bool:
        m, n = len(mat), len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j]==target:
                    return True

        return False
    # TC ~ O(mn)
    

    # Better ~ BS on each row
    def searchMatrix2(self, mat: list[list[int]], target: int) -> bool:
        m, n = len(mat), len(mat[0])

        for i in range(m):
            low, high = 0, n-1

            while low <= high:
                mid = (low + high)//2

                if mat[i][mid]==target:
                    return True

                elif mat[i][mid]< target:
                    low = mid + 1

                else:
                    high = mid - 1

        return False
    # TC ~ O(m log n)
    

    # Optimal
    def searchMatrix3(self, mat: list[list[int]], target: int) -> bool:
        m, n = len(mat), len(mat[0])
        row, col = 0, n-1

        while row < m and col >= 0:
            if mat[row][col] == target:
                return True

            elif mat[row][col] < target:
                row+=1

            else:
                col-=1

        return False
    # TC ~ O(log (m+n))
    

if __name__ == "__main__":
    matrix = [[1,4,7,11,15], [2,5,8,12,19], [3,6,9,16,22], [10,13,14,17,24], [18,21,23,26,30]]
    target = 5

    sol = Solution()
    # res = sol.searchMatrix(matrix, target)
    # res = sol.searchMatrix2(matrix, target)
    res = sol.searchMatrix3(matrix, target)

    print(res)