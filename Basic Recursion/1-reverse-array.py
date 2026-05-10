# reverse an array -- all approaches

# using two pointer without recursion
def reverse1(arr:list,l:int,r:int):
    while l<r:
        arr[l],arr[r]=arr[r],arr[l]
        l+=1
        r-=1
    return arr
# can even reverse any sub-array

# using one pointer without recursion
def reverse2(arr:list, i:int):
    n=len(arr)
    while i<n-i-1:
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
        i+=1
    return arr

# using two pointers + recursion
def reverse3(arr:list, l:int, r:int):
    if l<r:
        arr[l],arr[r]=arr[r],arr[l]
        reverse3(arr, l+1, r-1)
    return arr
# can even reverse any sub-array

# using one pointer + recursion
def reverse4(arr:list, i:int):
    n=len(arr)
    if i<=n//2:
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
        reverse4(arr,i+1)
    return arr


if __name__=="__main__":
    L=[2,3,6,5,7,1]
    n=len(L)  # 6
    # print(reverse1(L,0,4))
    # print(reverse2(L,0))
    print(reverse3(L,1,n-1))
    # print(reverse4(L,0))

