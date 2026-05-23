# Sort an array of O's, !'s and 2's

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

class Solution:
    # brute ~ using sort function

    # better
    def sortColors(self, nums: list[int]) -> None:
        res = []
        cnt0, cnt1, cnt2 = 0, 0, 0
        for i in nums:
            if i==0:
                cnt0+=1
            elif i==1:
                cnt1+=1
            else:
                cnt2+=1

        for i in range(cnt0):
            res.append(0)

        for i in range(cnt0, cnt0+cnt1):
            res.append(1)

        for i in range(cnt0+cnt1, cnt0+cnt1+cnt2):
            res.append(2)
        
        print(f"Resultant Array: {res}")
        # TC ~ O(2n), SC ~ O(n)

    # optimal ~ Dutch National Flag Algorithm
    def sortColors2(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums)-1

        while mid<=high:
            # using mid pointer
            if nums[mid]==0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low+=1
                mid+=1

            elif nums[mid]==1:
                mid+=1

            elif nums[mid]==2:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1
        
        print(f"Resultant Array: {nums}")
    # TC ~ O(n), SC ~ O(1)

if __name__=="__main__":
    arr = list(map(int,input().split()))
    
    sol = Solution()
    # sol.sortColors(arr)
    sol.sortColors2(arr)