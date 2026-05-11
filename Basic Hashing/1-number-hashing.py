# Number Hashing
def numHash1()->None:
    n=int(input())  # size of array
    arr=[]
    for _ in range(n):
        arr.append(int(input()))
    
    # pre-compute
    atmax=int(input())    # max value that can be stored
    hash_arr=[]
    for _ in range(atmax+1):
        hash_arr.append(0)

    for i in range(n):
        hash_arr[arr[i]]+=1

    # fetch
    q=int(input())  # No. of queries
    while q>0:
        num=int(input())
        print(f"Frequency of {num}:",hash_arr[num])
        q-=1
    
    # sample input 
    # 5
    # 1
    # 2
    # 2
    # 3
    # 4
    # 12
    # 4
    # 1
    # 2
    # 4
    # 5

# better
def numHash2() -> None:
    arr = list(map(int, input().split()))

    atmax = int(input())
    hash_arr = [0] * (atmax + 1)

    for num in arr:
        hash_arr[num] += 1

    q = int(input())

    for _ in range(q):
        num = int(input())
        print(f"Frequency of {num} --> {hash_arr[num]}")

    # sample input
    # 1 2 2 3 4
    # 12
    # 4
    # 1
    # 2
    # 4
    # 5
# optimal
from collections import Counter
def numHash3():
    # Take array input
    arr = list(map(int, input().split()))

    freq = Counter(arr)

    q = int(input())

    for _ in range(q):
        num = int(input())
        print(f"Frequency of {num} --> {freq[num]}")

if __name__=="__main__":
    # numHash1()
    # numHash2()
    numHash3()