# Next permutation of an array

# Brute ~ Generate all permutations, apply linear search for the given permutation and print the just next permutation
# T.C ~ O(n*n!) + O(n)

# Optimal approach
# Observation -->
# 1. Figure out the breakpoint/dip by making the longest prefix match
# 2. Find someone slightly > element at dipping index, but the smallest one so that you stay close
# 3. To keep the number as small as possible, sort the rest in ascending order

class Solution:
    def nextPermutation(self, nums: list[int]):
        n = len(nums)
        ind = -1      
        # to find the index from back at which dip comes
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind = i
                break

        if ind==-1:
            # If no dip that means last permutation is given 
            # so just fallback to first permutation
            nums[:] = nums[::-1]
            return nums

        for i in range(n-1,ind,-1):
            if nums[i]>nums[ind]:
                # swap
                nums[ind], nums[i] = nums[i], nums[ind]
                break
        
        # reverse the remaining sorted array
        nums[ind+1:] = nums[-1:ind:-1]

        return nums

if __name__=="__main__":
    arr = list(map(int, input().split()))
    sol = Solution()
    res = sol.nextPermutation(arr)
    print(f"Next permutation of array is {res}")