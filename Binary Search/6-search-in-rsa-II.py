# Search in Rotated Sorted Array - I
# Array may consist of DUPLICATE elements

# Solve in terms of UNIQUE and then figure out where it falis

class Solution:
    def searchRSA2(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        low, high = 0, n-1
        ans = False

        while low<=high:
            mid = (low + high) // 2

            # when element is found
            if nums[mid]==target:
                ans = True
                break

            # step-0: observe the crucial edge case when arr[low] == arr[mid] == arr[high] and handle it
            # step-1: identify the sorted/unsorted half
            # step-2: eliminate the adequate half where element is not present

            if nums[low] == nums[mid] and nums[mid]== nums[high]:
                # trim down the search space
                low+=1
                high-=1
                continue

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
# TC ~ O(log n) in average case, O(n/2) in worst case

if __name__=="__main__":
    arr = list(map(int, input().split()))
    x = int(input())

    sol = Solution()

    res = sol.searchRSA2(arr,x)
    if res==0:
        print("Target not present in RSA")
    else:
        print(f"Target is present in RSA")