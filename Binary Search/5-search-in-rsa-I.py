# Search in Rotated Sorted Array - I
# Array consists of UNIQUE elements

class Solution:
    def searchRSA(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n-1
        ans = -1

        while low<=high:
            mid = (low + high) // 2

            # when element is found
            if nums[mid]==target:
                ans = mid
                break

            # step-1: identify the sorted/unsorted half
            # step-2: eliminate the adequate half where element is not present

            # if left half is sorted
            if nums[low] <= nums[mid]:
                # eliminate right half if element somewhere present in between
                if nums[low]<=target and target<=nums[mid]:
                    high = mid - 1
                
                else:
                    low = mid + 1

            # if right half is sorted ~ (performing same type of operation in opposite fashion)
            else:
                # eliminate left half if element somewhere present in between
                if nums[mid]<=target and target<=nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            
        return ans


if __name__=="__main__":
    arr = list(map(int, input().split()))
    x = int(input())

    sol = Solution()

    res = sol.searchRSA(arr,x)
    if res==-1:
        print("Target not present in RSA")
    else:
        print(f"Target is present at index {res} in RSA")