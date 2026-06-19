# Peak Element in an array
# It's an element that is strictly greater than its neighbors.

class Solution:
    # Brute
    def findPeak(self, nums: list[int]) -> int:
        n = len(nums)

        for i in range(n):
            # if i==0:
            #     if nums[i]>nums[i+1]:
            #         return i
                
            # elif i==n-1:
            #     if nums[i]>nums[i-1]:
            #         return i
                
            # else:
            #     if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
            #         return i

            if (i==0 or nums[i-1]<nums[i]) and (i==n-1 or nums[i]>nums[i+1]):
                return i
        
        return -1
    
    # Optimal ~ BS --> For one peak
    def findPeak2(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Special cases
        if n==1:
            return 0
        
        if nums[0]>nums[1]:
            return 0
        
        if nums[n-1]>nums[n-2]:
            return n-1
        
        # Trimming down the search space for handling other cases
        low, high = 1, n-2
        while low<=high:
            mid = (low + high)//2

            # check if the middle index points to the peak element
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            
            # If we are on the increasing curve (or on the left side of peak)
            elif nums[mid]>nums[mid-1]:
                # eliminate left half (and go to search on right side)
                low = mid + 1

            # Else we are on the decreasing curve (or on the right side of peak)
            elif nums[mid]>nums[mid+1]:
                # eliminate right half (and go to search on left side)
                high = mid - 1

        return -1
    
    # Optimal ~ BS --> For multiple peaks
    def findPeak3(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Special cases
        if n==1:
            return 0
        
        if nums[0]>nums[1]:
            return 0
        
        if nums[n-1]>nums[n-2]:
            return n-1
        
        # Trimming down the search space for handling other cases
        low, high = 1, n-2
        while low<=high:
            mid = (low + high)//2

            # check if the middle index points to the peak element
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            
            # If we are on the increasing curve (or on the left side of peak)
            elif nums[mid]>nums[mid-1]:
                # eliminate left half (and go to search on right side)
                low = mid + 1

            # Else we are on the decreasing curve (or on the right side of peak)
            elif nums[mid]>nums[mid+1]:
                # eliminate right half (and go to search on left side)
                high = mid - 1

            # If we are standing on a local minimum
            else:
                # we can either go to left or to right
                # in our case we'll find the first peak
                high = mid - 1

        return -1


if __name__=="__main__":
    arr = list(map(int, input().split()))

    sol = Solution()
    # print(f"Peak Element Index: {sol.findPeak(arr)}")
    # print(f"Peak Element Index: {sol.findPeak2(arr)}")
    print(f"Peak Element Index: {sol.findPeak3(arr)}")