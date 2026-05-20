# Two Sum
# Variety 2 -> Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

from collections import Counter
class Solution:
    # brute force
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1,n):
                if target == nums[i]+nums[j]:
                    return [i,j]
        return [-1,-1]
    # TC ~ O(n^2), SC ~ O(1)

    # optimal
    def twoSum2(self, nums:list, target:int):
        n = len(nums)
        hash_map = {}
        for i in range(n):
            el = nums[i]
            needed = target - el

            if needed in hash_map:
                return [hash_map[needed],i]
            
            hash_map[el] = i
        
        return [-1,-1]
    # TC ~ O(n), SC ~ O(n)


if __name__=="__main__":
    arr = list(map(int, input().split()))
    t = int(input())

    sol = Solution()

    # print(sol.twoSum(arr,t))
    print(sol.twoSum2(arr,t))
