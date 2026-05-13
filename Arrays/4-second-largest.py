# Find second largest element in the array
# brute force ~ get 2nd largest after sorting
def secondLargestEl(nums:list)->int:
    nums.sort()
    for i in range(len(nums)-2,-1,-1):
        if nums[i]<nums[-1]:
            return nums[i]
    return -1
# O(n logn + n)
                
# better ~ largest and second largest separately
def secondLargestEl2(nums:list)->int:
    lar,secL=max(nums),-1
    for i in range(len(nums)):
        if nums[i]>secL and nums[i]!=lar:
            secL=nums[i]
    return secL
# O(2n)

# optimal ~ in one pass
def secondLargestEl3(nums:list)->int:
    lar,secL=arr[0],-1
    for i in range(1,len(nums)):
        if nums[i]>lar:
            secL=lar
            lar=nums[i]
        elif nums[i]<lar and nums[i]>secL:
            secL=nums[i]
    return secL
# O(n)

if __name__=="__main__":
    arr=list(map(int, input().split()))
    # print(secondLargestEl(arr))
    # print(secondLargestEl2(arr))
    print(secondLargestEl3(arr))