# Longest Consecutive Sequence (Medium-Hard)
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

from cmath import inf
class Solution:
    # brute
    # helper
    def linearSearch(self, nums:list[int], k:int)-> bool:
        for i in nums:
            if i==k:
                return True
        return False

    def longestConsSeq(self, nums:list[int])-> int:
        n = len(nums)
        longest = 1
        for i in range(n):
            el = nums[i]
            cntCons = 1
            while self.linearSearch(nums,el+1):
                el = el+1
                cntCons += 1
            
            longest = max(longest, cntCons)

        return longest
    # TC ~ O(n^2) as for each element we are doing linear search in worst case
    # SC ~ O(1) as we are not using any extra space

    # better ~ includes distortion of input array
    def longestConsSeq2(self, nums:list[int]):
        nums.sort()
        longest = 1
        last_smaller = -inf    # to keep track of last smallest element
        cntCur = 0             # to keep track of numbers in current sequence

        for i in nums:
            if i-1==last_smaller:
                cntCur += 1
                last_smaller = i

            elif i!=last_smaller:
                cntCur = 1
                last_smaller = i

            longest = max(longest, cntCur)

        return longest
    # TC ~ O(nlogn) as we are sorting the array
    # SC ~ O(1) as we are not using any extra space
    
    # optimal
    def longestConsSeq3(self, nums:list[int]):
        n = len(nums)
        longest = 1
        s = set(nums)    # to store the elements in a set for O(1) search

        for i in s:
            if i-1 not in s:    # if i is the start of a sequence
                cnt = 1
                el = i
                while el+1 in s:    # count the length of the sequence
                    cnt += 1
                    el = el+1
                
                longest = max(longest, cnt)

        return longest
    # TC ~ O(3n) as we are traversing the array once to create the set, then traversing the set and in worst case traversing the set again for counting the length of sequence
    # SC ~ O(n) as we are using a set to store the elements of the

if __name__=="__main__":
    arr = list(map(int, input().split()))

    sol = Solution()

    # res = sol.longestConsSeq(arr)
    # res = sol.longestConsSeq2(arr)
    res = sol.longestConsSeq3(arr)

    print(f"Length of Longest Consecutive Sequence: {res}")