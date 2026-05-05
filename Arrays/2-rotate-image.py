# Rotate Image / Rotate nxn matrix by 90 degrees
from typing import List
# brute force ~ O(n^2), O(n^2)
class Solution:
    def rotateImage(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Create a new matrix of same size to store rotated result
        rotated = [[0] * n for _ in range(n)]

        # Traverse each element of original matrix
        for i in range(n):
            for j in range(n):
                # Place the element at its new rotated position
                rotated[j][n - i - 1] = matrix[i][j]

        # Return the rotated matrix
        return rotated

# optimal ~ O(n^2), O(1)
class Solution2:
    def rotateImage(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose the 2D matrix
        n=len(matrix)
        for i in range(n-1):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j] 
        
        # reverse each row of matrix
        for i in range(n):
            matrix[i]=matrix[i][::-1]
        return matrix
        
# driver
if __name__ == "__main__":
    sol = Solution2()
    arr2D=[
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rot_res = sol.rotateImage(arr2D)
    # Print the rotated matrix
    for row in rot_res:
        print(row)