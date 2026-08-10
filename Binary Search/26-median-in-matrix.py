# Median in Row-wise sorted matrix (Medium)

class Solution:
    # brute
    def median2D(self, mat:list[list[int]])-> int:
        n, m = len(mat), len(mat[0])
        arr = []
        for i in range(n):
            for j in range(m):
                arr.append(mat[i][j])
                
        arr.sort()
         
        return arr[n*m // 2]
    # TC ~ O(n*m + (n*m)log(n*m))

    # better ~ O(2nm)

    # optimal
    def upperBound(self, nums:list[int], x:int)-> int:
            # Smallest index such that arr[ind] > x 
            # it tells how many numbers are smaller than number 'x' in array

            n = len(nums)
            low, high = 0, n-1
            ans = n
    
            while low<=high:
                mid = (low + high) // 2
                if nums[mid] > x:
                    # may be an answer
                    ans = mid
                    # look on left for smallest index
                    high = mid - 1
    
                else:
                    low = mid + 1
            
            return ans
    
    def median2D_op(self, mat:list[list[int]])-> int:
        def blackBox(mat, x):
            # how many numbers are smaller than number 'x' in matrix
            cnt = 0
            for row in mat:
                cnt += self.upperBound(row,x)

            return cnt
        
        n, m = len(mat), len(mat[0])
        low, high = float('inf'), float('-inf')
        
        for i in range(n):
            low = min(low, mat[i][0])
            high = max(high, mat[i][-1])

        while low<=high:
            mid = (low + high)//2

            smallerEquals = blackBox(mat,mid)

            if smallerEquals <= (n*m)//2:
                # we're on the left side and need to search on the right side
                low = mid + 1

            else:
                # we're on the right side and need to search on the left side
                high = mid - 1

        return low
    # TC ~ O(n log(max-min) * log m)

if __name__=="__main__":
    matrix = [[1,4,7,11,15], [2,5,8,11,19], [3,6,9,10,22], [9,14,16,17,24], [14,21,23,26,30]]

    sol = Solution()

    # res = sol.median2D(matrix)
    res = sol.median2D_op(matrix)

    print(res)