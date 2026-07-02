# Painter's Partition / Split Array Largest Sum

# Given an integer array nums and an integer k, 
# split nums into k non-empty subarrays such that 
# the largest sum of any subarray is minimized.
# Return the minimized largest sum of the split.

class Solution:
    def countSubarrays(self, arr, fixedSum):
        count = 1
        lastSubSum = arr[0]
        
        for i in range(1,len(arr)):
            if lastSubSum + arr[i] <= fixedSum:
                lastSubSum += arr[i]

            else:
                count += 1
                lastSubSum = arr[i]

        return count
    
    def splitArray(self, nums: list[int], k: int) -> int:
        if len(nums)<k:
            return -1
        
        lower_limit = max(nums)
        upper_limit = sum(nums)
        for subSum in range(lower_limit,upper_limit+1):
            subarrays = self.countSubarrays(nums, subSum)
            if subarrays <= k:
                return subSum

        return lower_limit

    def splitArray2(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low <= high:
            mid = (low + high) // 2

            if self.countSubarrays(nums, mid) > k:
                low = mid + 1
            else:
                high = mid - 1

        return low

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    k = int(input())

    sol = Solution()

    # res = sol.splitArray(arr,k)
    res = sol.splitArray2(arr,k)

    print(f"Minimized Largest Sum of the Split: {res}") 
