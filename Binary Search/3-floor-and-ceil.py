# Floor and Ceil in sorted array

# Floor : largest no. in array <= x  (ground)
# Ceil : Smallest no. in array >= x  (top)

class Solution:
    def floor(self, nums:list[int], x:int)-> int:
        n = len(nums)
        low, high = 0, n-1
        ans = -1

        while low<=high:
            mid = (low + high) // 2
            if nums[mid] <= x:
                # may be an answer
                ans = nums[mid]
                # look on right for largest number
                low = mid + 1

            else:
                high = mid - 1
        
        return ans
    
    def ceil(self, nums:list[int], x:int)-> int:
        n = len(nums)
        low, high = 0, n-1
        ans = -1

        while low<=high:
            mid = (low + high) // 2
            if nums[mid] >= x:
                # may be an answer
                ans = nums[mid]
                # look on left for smallest number
                high = mid - 1

            else:
                low = mid + 1
        
        return ans
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    x = int(input())
    sol = Solution()

    print(f"Floor of {x} in array: {sol.floor(arr,x)}")
    print(f"Ceil of {x} in array: {sol.ceil(arr,x)}")