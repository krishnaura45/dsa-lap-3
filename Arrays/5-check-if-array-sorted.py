# Check whether the array/list is sorted or not
def isSorted(nums:list) -> bool:
    for i in range(1,len(nums)):
        if nums[i]>=nums[i-1]: pass
        else:
            return False
    return True


# Leetcode variation ~ solution
# Check whether array was originally sorted and rotated by some x places now or not (where x ~ (0,n))
def isSortedRotated(nums:list) -> bool:
    n = len(nums)
    count = 0     # Number of discontinuity when sorted and not rotated
    
    for i in range(n):
        # an array if sorted, and if rotated left/right, then we'll surely find discontinuity --> // or \\, for eg: 12345 -> 45|123
        if nums[i] > nums[(i + 1) % n]:
            count += 1
    
    return (count <= 1)

if __name__=="__main__":
    arr=list(map(int, input().split()))
    print(isSorted(arr))