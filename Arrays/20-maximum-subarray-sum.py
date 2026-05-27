# Maximum Subarray Sum
# Find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution:

    # brute force
    def maxSubArray(self, nums: list[int]) -> int:
        maxi = float('-inf')
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                sum = 0
                for k in range(i,j+1):
                    sum+=nums[k]

                if sum > maxi:
                    maxi = sum

        return maxi

    # better
    def maxSubArray2(self, nums: list[int]) -> int:
        maxi = float('-inf')
        for i in range(len(nums)):
            sum = 0
            for j in range(i,len(nums)):
                sum+=nums[j]
                maxi = max(maxi, sum)
        return maxi
    # TC ~ O(n^2), SC ~ O(1)

    # optimal ~ Kadane's Algorithm
    def maxSubArray3(self, nums: list[int]) -> int:
        # using kadane's algo
        maxi = nums[0]
        sum = 0
        for i in range(len(nums)):
            sum+=nums[i]

            if sum > maxi:
                maxi = sum

            if sum < 0:
                sum = 0

        return maxi
    # TC ~ O(n), SC ~ O(1)

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    sol = Solution()

    # print(sol.maxSubArray(arr))
    # print(sol.maxSubArray2(arr))
    print(sol.maxSubArray3(arr))