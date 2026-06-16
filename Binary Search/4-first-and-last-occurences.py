# First and Last occurences of an element in sorted array

# Linear time
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        first, last = -1, -1

        for i in range(n):
            if nums[i] == target:
                if first == -1:
                    first = i

                last = i
        
        return [first, last]
    

# Binary Search - I    
class Solution2:
    # helpers
    def lowerBound(self, nums:list[int], x:int)-> int:
        n = len(nums)
        low, high = 0, n-1
        ans = n

        while low<=high:
            mid = (low + high) // 2
            if nums[mid] >= x:
                ans = mid
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
                ans = mid
                high = mid - 1

            else:
                low = mid + 1
        
        return ans

    # logic
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        lb = self.lowerBound(nums, target)
        ub = self.upperBound(nums, target)

        # if target is either not present or its lower bound pointing to hypothetical index 'n'
        if lb==n or nums[lb]!=target:
            return [-1,-1]

        return [lb, ub-1] 
    

# Binary Search - II
class Solution3:
    def firstPosition(self, nums, x):
        n = len(nums)
        first = -1
        low, high = 0, n-1

        while low<=high:
            mid = (low + high) // 2
            if nums[mid]==x:
                first = mid
                high = mid - 1
            
            elif nums[mid]>x:
                high = mid - 1

            else:
                low = mid + 1

        return first

    def lastPosition(self, nums, x):
        n = len(nums)
        last = -1
        low, high = 0, n-1
        while low<=high:
            mid = (low + high) // 2
            if nums[mid]==x:
                last = mid
                low = mid + 1

            elif nums[mid]<x:
                low = mid + 1
            
            else:
                high = mid - 1

        return last

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return [self.firstPosition(nums, target), self.lastPosition(nums, target)] 
        
    
if __name__ == "__main__":
    arr = list(map(int, input().split()))
    x = int(input())

    # sol = Solution()
    # print(f"Floor of {x} in array: {sol.searchRange(arr,x)}")

    # sol = Solution2()
    # print(f"Floor of {x} in array: {sol.searchRange(arr,x)}")

    sol = Solution3()
    print(f"First and Last Position of {x} in array: {sol.searchRange(arr,x)}")