# Longest Subarray with sum K [Postives and Negatives]

class Solution:
    # brute ~ using nested loops
    
    # optimized brute
    def longestSubarray(self, nums:list, k:int)->int:
        max_len = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i,len(nums)):
                s+=nums[j]
                if s==k:
                    max_len = max(max_len, j-i+1)    
        return max_len
    # TC ~ O(n^2), SC ~ O(1)

    # optimal ~ using hashmap/dictionary
    def longestSubarray2(self, nums:list, k:int)->int:
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

if __name__=="__main__":
    sol = Solution()

    arr = list(map(int, input().split()))
    k = int(input())

    # Test Case 1
    # arr = [1 2 2 -1 1 1 2]
    # k = 3

    # Test Case 2
    # arr = [2 0 1 -1 1 6 -3 3 1 2]
    # k = 3

    # res = sol.longestSubarray(arr, k)
    res = sol.longestSubarray2(arr, k)

    print(f"Length of longest subarray with sum {k}: {res}")