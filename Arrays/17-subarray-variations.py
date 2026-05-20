# Leetcode variation-1 : Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray of which the sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

class Solution1:
    def minSubArrayLen(self, target:int, nums:list):
        n = len(nums)
        min_len = n+1
        left,right = 0,0
        s = nums[0]    # sum of the current frame
        while right<n:
            # If sum >= target, trim the frame from the left until sum = k
            while left<=right and s>=target:
                min_len = min(min_len, right-left+1)
                s-=nums[left]
                left+=1

            right+=1
            if right<n:
                s+=nums[right]

        if min_len<=n:
            return min_len
        else:
            return 0
        

# Leetcode variation-2 : Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

class Solution2:
    def subarraySum(self, nums:list, k:int)->int:
        count = 0
        s = 0
        preSumMap = {0:1}   # prefix sum and its frequency
        for i in range(len(nums)):
            s+=nums[i]

            remaining_sum = s-k
            if remaining_sum in preSumMap:
                count+=preSumMap[remaining_sum]
            
            if s in preSumMap:
                preSumMap[s]+=1
            else:
                preSumMap[s] = 1
        
        return count