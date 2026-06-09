class Solution:
    def insertionSort(self, nums: list[int])-> list[int]:
        """
        Take an element at a time, and 
        place it at its correct position of order by adjacent swaps
        """
        n = len(nums)

        for i in range(1,n):
            j = i
            while j>0 and nums[j-1]>nums[j]:
                # swap adjacent elements
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j-=1

        return nums

if __name__=="__main__":
    arr = list(map(int, input().split()))
    obj = Solution()
    res = obj.insertionSort(arr)
    print(res)