# Find the number in array that appears once where all other elements appear twice

from collections import Counter
class Solution:
    # brute ~ Iterate through the array and count the frequency of each element, if frequency is 1 then return that element
    def uniqueOccurrence1(self, nums:list)-> int:
        for i in range(len(nums)):
            cnt = 0
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    cnt+=1
            if cnt==1:
                return nums[i]
    # TC, SC ~ O(n^2), O(1)

    # better
    def uniqueOccurrence2(self, nums:list):
        # get the maximum
        maxi = nums[0]
        for i in nums:
            maxi = max(maxi,i)
        
        # hashing
        hash_arr = [0] * (maxi+1)
        for i in nums: hash_arr[i]+=1

        # get the single element
        for i in nums:
            if hash_arr[i]==1:
                return i    
    # TC, SC ~ O(3n), O(k) where k is the number of unique elements

    # more better
    def uniqueOccurrence3(self, nums:list):
        freq = Counter(nums)
        for i in nums:
            if freq[i]==1:
                return i
    # TC, SC ~ O(2n), O(k) where k is the number of unique elements

    # optimal
    def uniqueOccurrence(self, nums:list):
        xor_arr = 0
        for i in nums:
            xor_arr ^= i

        return xor_arr
    # TC ~ O(n)
    # SC ~ O(1)

if __name__=="__main__":
    sol = Solution()
    arr = list(map(int, input().split()))
    # res = sol.uniqueOccurrence1(arr)
    # res = sol.uniqueOccurrence2(arr)
    # res = sol.uniqueOccurence3(arr)
    res = sol.uniqueOccurrence(arr)
    print(f"Number appearing once: {res}")