# I - Left rotate an array by one place
# optimal solution  
def leftRotate(nums:list):
    temp = nums[0]
    for i in range(1, len(nums)):
        nums[i-1] = nums[i]
    nums[-1] = temp
    print(f"Left Rotated array by one place: {nums}")


# II - Left rotate an array by k places
# Sol 1
def leftRotateK(nums:list, k:int):
    n = len(nums)
    d = k  # to store original k as asked in problem
    k = k % n
    temp = nums[:k+1]   # slicing --> take first k elements into a temporary array
    # shifting of n-k elements to left in original array
    for i in range(k, n):
        nums[i-k] = nums[i]
    
    # Put sliced elements in-place to the right of shifted elements
    # for i in range(n-k,n):
    #     nums[i] = temp[i-(n-k)]
    nums[n-k:n] = temp[:k]
    
    print(f"Left Rotated array by {d} places: {nums}")
# TC, SC ~ O(n+k), O(k) --> Less Runtime, Taking extra space

# Sol 2
# helper function
def reverse(arr:list,l:int,r:int):
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr

def leftRotateK2(nums:list,k:int):
    n = len(nums)
    d, k = k, k % n

    # perform three reverse operations
    reverse(nums,0,k-1)   # first k elememts
    reverse(nums,k,n-1)   # other n-k elements
    reverse(nums,0,n-1)   # n elements

    print(f"Left Rotated array by {d} places: {nums}")
# TC, SC ~ O(2n), O(1) --> Memory efficient, More runtime

if __name__=="__main__":
    arr=list(map(int, input().split()))
    # leftRotate(arr)
    # leftRotateK(arr,3)
    leftRotateK2(arr,7)