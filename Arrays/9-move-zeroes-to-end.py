# Move Zeroes to end
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

class Solution:
    # brute force 
    def moveZeroes(self, nums:list):
        n = len(nums)
        # storing non-zero elements in another array
        temp = []
        for i in range(n):
            if nums[i]!=0: temp.append(nums[i])
        
        k = len(temp)        # no. of non-zero elements
        # Replacing first k elements with non-zero elements
        nums[:k] = temp[:k]
        
        # Replacing the last n-k elements with 0
        nums[k:n] = [0] * (n-k)
        
        print(f"Modified Array: {nums}")
    
    # TC, SC ~ O(2n), O(k)

    # optimal ~ Using two pointers
    def moveZeroes2(self, nums:list):
        n = len(nums)

        j = -1
        # To get index of first zero
        for i in range(n):
            if nums[i] == 0:
                j = i
                break
        
        if j == -1:
            # no zeroes found
            pass
        else:
            # If zeroes found, shift zeroes to right
            for i in range(j+1,n):
                if nums[i] != 0:
                    # perform swap
                    nums[j],nums[i] = nums[i],nums[j]
                    j += 1

        print(f"Modified Array: {nums}")
    # TC, SC ~ O(n), O(1)
        

if __name__=="__main__":
    arr = list(map(int,input().split()))
    sol = Solution()
    # sol.moveZeroes(arr)
    sol.moveZeroes2(arr)
