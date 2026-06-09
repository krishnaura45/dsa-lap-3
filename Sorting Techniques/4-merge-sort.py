class Solution:
    def merge(self, nums:list[int], low:int, mid:int, high:int)-> None:
        left, right = low, mid+1
        temp = []

        while left<=mid and right<=high:
            if nums[left]<=nums[right]:
                temp.append(nums[left])
                left+=1

            else:
                temp.append(nums[right])
                right+=1

        while left<=mid:
            temp.append(nums[left])
            left+=1

        while right<=high:
            temp.append(nums[right])
            right+=1

        # insert from temporary to original array
        for i in range(low,high+1):
            nums[i] = temp[i - low]


    def mergeSort(self, nums: list[int], low:int, high:int)-> None:
        """
        Divide the array into two halves, sort them recursively and then merge the sorted halves.

        Input: nums - list of integers to be sorted
               low - starting index of the array
               high - ending index of the array
        """
        # base case
        if low>=high:
            return

        # core logic ~ divide and merge
        mid = (low+high)//2     # middle index of array
        self.mergeSort(nums,low,mid)
        self.mergeSort(nums,mid+1,high)
        self.merge(nums,low,mid,high)
        

if __name__=="__main__":
    arr = list(map(int, input().split()))
    n = len(arr)
    obj = Solution()
    obj.mergeSort(arr,0,n-1)
    print(arr)