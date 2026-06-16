# Minimum in Roatated Sorted Array

class Solution:
    # brute BS
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        ans = float('inf')

        low, high = 0, n-1
        while low<=high:
            mid = (low + high)//2

            # if left half is sorted
            if nums[low] <= nums[mid]:
                ans = min(nums[low], ans)
                low = mid + 1

            # otherwise right half would be sorted
            else:
                ans = min(nums[mid], ans)
                high = mid - 1

        return ans
    
    # optimal BS ~ slightly better TC
    def findMin2(self, nums: list[int]) -> int:
        n = len(nums)
        ans = float('inf')

        low, high = 0, n-1
        while low<=high:
            mid = (low + high)//2

            # if both halves are sorted after some operations then arr[low] will always be smaller
            if nums[low] <= nums[high]:
                ans = min(ans, nums[low])
                break

            # if left half is sorted
            if nums[low] <= nums[mid]:
                # update minimum
                ans = min(nums[low], ans)
                # eliminate this half
                low = mid + 1

            # otherwise right half would be sorted
            else:
                ans = min(nums[mid], ans)
                high = mid - 1

        return ans
    
if __name__=="__main__":
    arr = list(map(int, input().split()))
    sol = Solution()
    print(f"Minimum in RSA: {sol.findMin2(arr)}")