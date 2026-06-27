# Find the smallest divisor given a threshold (same as KOKO Eating Bananas)

import math
class Solution:
    # brute ~ linear search aligned
    def smallestDivisor(self, nums: list[int], t: int) -> int:
        pass

    # optimal ~ binary search aligned
    def divSum(self, nums, divisor):
        divsum = 0
        for i in nums:
            divsum += math.ceil(i/divisor)
        
        return divsum

    def smallestDivisor2(self, nums: list[int], threshold: int) -> int:
        low, high = 1, max(nums)

        while low<=high:
            mid = (low + high) // 2
            
            # deciding condition
            if self.divSum(nums,mid) <= threshold:
                high = mid - 1

            else:
                low = mid + 1

        return low

if __name__=="__main__":
    arr = list(map(int,input().split()))
    threshold = int(input())

    sol = Solution()

    res = sol.smallestDivisor2(arr,threshold)

    print(f"Smallest Divisor: {res}")