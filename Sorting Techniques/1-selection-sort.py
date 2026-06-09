class Solution:
    def selectionSort(self, nums: list[int])-> list[int]:
        """
        Find the minimum from the elements of left unsorted array and swap it with the first position element of the same
        """
        n = len(nums)
        for i in range(n-1):
            # find index of the minimum element in left unsorted array
            mini = i
            for j in range(i,n):
                if nums[j]<nums[mini]:
                    mini = j
            
            # swap the current with minimum element
            nums[i], nums[mini] = nums[mini], nums[i]

        return nums

if __name__=="__main__":
    arr = list(map(int, input().split()))
    obj = Solution()
    res = obj.selectionSort(arr)
    print(res)