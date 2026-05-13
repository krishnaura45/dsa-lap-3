# Find largest element in the array
# brute force ~ sort and get last element
def largestEl(nums:list)->int:
    nums.sort()
    return nums[-1]
# O(n logn)
                
# optimal ~ direct using in-built function
def largestEl2(nums:list)->int:
    return max(nums)
# O(n)

# optimal ~ using loop
def largestEl3(nums:list)->int:
    lar=arr[0]
    for i in range(1,len(nums)):
        if nums[i]>lar: lar=arr[i]
    return lar
# O(n)

if __name__=="__main__":
    arr=list(map(int, input().split()))
    # print(largestEl(arr))
    # print(largestEl2(arr))
    print(largestEl3(arr))
