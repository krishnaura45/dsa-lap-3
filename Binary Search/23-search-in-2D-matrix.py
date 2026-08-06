# Problem:
# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

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
    

    # Optimal ~ Hypothetically flatten 2D matrix into 1D array and run BS
    def searchMatrix3(self, mat: list[list[int]], target: int) -> bool:
        m, n = len(mat), len(mat[0])

        low, high = 0, m * n - 1

        while low <= high:
            mid = (low + high) // 2

            row = mid // n
            col = mid % n

            if mat[row][col] == target:
                return True

            elif mat[row][col] < target:
                low = mid + 1

            else:
                high = mid - 1

        return False
    # TC ~ O(log mn)
    

if __name__ == "__main__":
    matrix = [[1, 2, 4, 6], [7, 8, 9, 10], [11, 12, 15, 16]]
    target = 12

    sol = Solution()
    # res = sol.searchMatrix(matrix, target)
    # res = sol.searchMatrix2(matrix, target)
    res = sol.searchMatrix3(matrix, target)

    print(res)
