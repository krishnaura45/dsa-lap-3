# I - Right rotate an array by one place
# optimal solution  
def rightRotate(nums:list):
    n = len(nums)
    temp = nums[-1]
    for i in range(n-2,-1,-1):
        nums[i+1] = nums[i]
    nums[0] = temp
    print(f"Right Rotated array by one place: {nums}")


# II - Right rotate an array by k places
# brute
def rightRotateK(nums:list, k:int):
    n = len(nums)
    d, k = k, k % n
    temp = nums[-k:]   # slicing --> take last k elements into a temporary array
    # shifting of n-k elements to right in original array
    for i in range(n-k-1,-1,-1):
        nums[i+k] = nums[i]
    
    # Put sliced elements in-place to the left of shifted elements
    # for i in range(k):
    #     nums[i] = temp[i]
    nums[:k] = temp[:k]
    
    print(f"Right Rotated array by {d} places: {nums}")

# optimal
# helper function
def reverse(arr:list,l:int,r:int):
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr

def rightRotateK2(nums:list,k:int):
    n = len(nums)
    d, k = k, k % n

    # perform three reverse operations
    reverse(nums,0,n-1)   # n elements
    reverse(nums,0,k-1)   # first k elememts
    reverse(nums,k,n-1)   # other n-k elements

    print(f"Right Rotated array by {d} places: {nums}")

if __name__=="__main__":
    arr=list(map(int, input().split()))
    # rightRotate(arr)
    # rightRotateK(arr,3)
    rightRotateK2(arr,10)