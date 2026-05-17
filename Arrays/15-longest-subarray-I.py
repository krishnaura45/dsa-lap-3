# Longest Subarray with given Sum K (Zero and Positives)
# Subarray ~ Contiguous part of the array

class Solution:
    # brute ~ using nested loops
    def longestSubarray(self, nums:list, k:int)->int:
        max_len = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                # s = 0
                # for idx in range(i,j+1):
                #     s+=nums[idx]

                s = sum(nums[i:j+1])

                if s==k:
                    max_len = max(max_len, j-i+1)    
        return max_len
    # TC ~ O(n^3), SC ~ O(1)
    
    # optimized brute
    def longestSubarray2(self, nums:list, k:int)->int:
        max_len = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i,len(nums)):
                s+=nums[j]
                if s==k:
                    max_len = max(max_len, j-i+1)    
        return max_len
    # TC ~ O(n^2), SC ~ O(1)

    # better ~ using hashmap/dictionary
    def longestSubarray3(self, nums:list, k:int)->int:
        max_len = 0
        s = 0
        preSumMap = {}
        for i in range(len(nums)):
            # prefix sum upto index i
            s+=nums[i]

            # If the sum = k, update the max length
            if s==k:
                max_len = max(max_len,i+1)

            remaining_sum = s-k
            # If remaining sum exists in map previously, then update the max length
            if remaining_sum in preSumMap:
                max_len = max(max_len,i-preSumMap[remaining_sum])
            
            # If the prefix sum was not there previously, then add it to the map with its index
            if s not in preSumMap:
                preSumMap[s] = i
        
        return max_len
    # TC ~ O(n), SC ~ O(n)

    # optimal ~ using two pointers
    def longestSubarray4(self, nums:list, k:int)->int:
        n = len(nums)
        max_len = 0
        left,right = 0,0
        s = nums[0]    # sum of the current frame
        while right<n:
            # If sum > k, trim the frame from the left until sum <= k
            while left<=right and s>k:
                s-=nums[left]
                left+=1
            
            if s==k:
                max_len = max(max_len, right-left+1)

            right+=1
            if right<n:
                s+=nums[right]
        
        return max_len

if __name__=="__main__":
    sol = Solution()

    arr = list(map(int, input().split()))
    k = int(input())

    # Test Case 1
    # arr = [1 2 3 1 1 1 1 4 2 3]
    # k = 3

    # Test Case 2
    # arr = [5 2 1 3 2 1 0 1 4]
    # k = 5

    # res = sol.longestSubarray(arr, k)
    # res = sol.longestSubarray2(arr, k)
    # res = sol.longestSubarray3(arr, k)
    res = sol.longestSubarray4(arr, k)

    print(f"Length of longest subarray with sum {k}: {res}")