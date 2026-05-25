# Majority Element
# Given an array of size n, find the element that appears more than ⌊ n/2 ⌋ times.

from collections import Counter
class Solution:
  # brute force
    def majorityElement(self, nums:list[int]) -> int:
        n = len(nums)
        for i in range(n):
            cnt = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    cnt+=1
            
            if cnt > n//2:
                return nums[i]

        return -1
    # TC ~ O(n^2), SC ~ O(1)

    # better ~ hashmap
    def majorityElement2(self, nums:list[int]) -> int:
        freq = Counter(nums)
        
        for key, value in freq.items():
            if value > len(nums)//2:
                return key
            
        return -1
    # TC ~ O(2n), SC ~ O(n)

    # optimal ~ Boyer-Moore Voting Algorithm
    def majorityElement3(self, nums:list[int]) -> int:
        count = 0
        el = None

        for i in nums:
            if count == 0:
                count = 1
                el = i

            elif i == el:
                count+=1

            else:
                count-=1
        
        # verify if el is the majority element
        count2 = 0
        for i in nums:
            if i == el:
                count2+=1   
            
        if count2 > len(nums)//2:
            return el
        
        return -1
    # TC ~ O(n), SC ~ O(1)

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    sol = Solution()

    # print(sol.majorityElement(arr))
    # print(sol.majorityElement2(arr))
    print(sol.majorityElement3(arr))