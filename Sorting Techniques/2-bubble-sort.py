from cmath import inf
class Solution:
    def bubbleSort(self, nums: list[int])-> list[int]:
        """
        Push the maximum to the last one by one by means of adjacent swaps
        """
        n = len(nums)
        didSwap = 0
        for i in range(n-1,0,-1):
            for j in range(i):
                if nums[j]>nums[j+1]:
                    # swap
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    # record the first swap
                    didSwap = 1

            # optimization to save time
            if didSwap == 0:
                # if no swap in first scan then that means array already sorted
                return nums

        return nums

if __name__=="__main__":
    arr = list(map(int, input().split()))
    obj = Solution()
    res = obj.bubbleSort(arr)
    print(res)