# Quick Sort
# This algorithm is basically a repetition of two simple steps that are the following:
# 1. Pick a pivot and place it in its correct place in the sorted array.
# 2. Shift smaller elements(i.e. Smaller than the pivot) on the left of the pivot and larger ones to the right.

class Solution:
    def partition(self, arr, low, high):
        pivot = arr[low]
        i, j = low, high

        while i < j:
            while i <= high - 1 and arr[i] <= pivot:
                i += 1

            while j >= low + 1 and arr[j] > pivot:
                j -= 1

            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]

        return j

    def qs(self, nums, low, high):

        if low >= high:
            return

        pIndex = self.partition(nums, low, high)

        self.qs(nums, low, pIndex - 1)
        self.qs(nums, pIndex + 1, high)

    def quickSort(self, nums):
        self.qs(nums, 0, len(nums) - 1)
        return nums
    
# TC ~ O(n log n) in average and best case but O(n^2) in worst case


if __name__=="__main__":
    arr = list(map(int, input().split()))
    obj = Solution()
    res = obj.quickSort(arr)
    print(res)