# Spiral Traversal of a Matrix
# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralVortex(self, matrix:list[list[int]])-> list[int]:
        m, n = len(matrix), len(matrix[0])
        ans = []

        left, right, top, bottom = 0, n-1, 0, m-1

        while top<=bottom and left<=right:
            # towards right-->
            for i in range(left, right+1):
                ans.append(matrix[top][i])
            top+=1

            # down -->
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
            right-=1

            # towards left-->
            if top<=bottom:
                # if still any row left to traverse
                for i in range(right, left-1, -1):
                    ans.append(matrix[bottom][i])
                bottom-=1

            # up -->
            if left<=right:
                # if still any column to traverse
                for i in range(bottom, top-1, -1):
                    ans.append(matrix[i][left])
                left+=1

        return ans

if __name__ == "__main__":
     mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
     
     sol = Solution()

     res = sol.spiralVortex(mat)

     print(res)