# Lower and Upper Bound of a number in a sorted array
# Lower Bound ~ Smallest index such that arr[ind] >= x
# Upper Bound ~ Smallest index such that arr[ind] > x

class Solution:
    def lowerBound(self, nums:list[int], x:int)-> int:
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
    
    def upperBound(self, nums:list[int], x:int)-> int:
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
    
    # variation ~ leetcode
    # Search Insert Position
    def searchInsertIndex(self, nums:list[int], x:int)-> int:
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
    
if __name__=="__main__":
    arr = list(map(int, input().split()))
    num = int(input())

    sol = Solution()

    lb = sol.lowerBound(arr, num)
    ub = sol.upperBound(arr, num)

    print(f"Lower Bound Index of {num} in array: {lb}")
    print(f"Upper Bound Index of {num} in array: {ub}")