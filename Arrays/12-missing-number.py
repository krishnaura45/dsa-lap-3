# Find missing number in the array of numbers from 1 to N
from collections import Counter
class Solution:
    # brute force ~ Check for each number from 1 to N if it is present in the array or not
    def missingNumber(self, nums:list, N:int):
        missing = -1
        for i in range(1,N+1):
            if i not in nums:
                missing = i
        return missing
    # TC ~ O(N^2), SC ~ O(1)

    # better
    def missingNumber2(self, nums:list, N:int):
        missing = -1
        freq = Counter(nums)
        for i in range(1, N + 1):
            if freq[i] == 0:
                missing = i
        return missing
    # TC ~ O(N), SC ~ O(N)

    # optimal ~ Using the formula for the sum of first N natural numbers, which is N*(N+1)/2. We can calculate the sum of the given array and subtract it from the expected sum to find the missing number.
    def missingNumber3(self, nums:list, N:int):
        expected_sum = N * (N + 1) // 2
        actual_sum = sum(nums)
        missing = expected_sum - actual_sum
        return missing
    # TC ~ O(N), SC ~ O(1)

if __name__=="__main__":
    sol = Solution()
    arr = list(map(int, input().split()))
    N = int(input())

    # res = sol.missingNumber(arr, N)
    # res = sol.missingNumber2(arr, N)
    res = sol.missingNumber3(arr, N)
    print(f"Missing number: {res}")