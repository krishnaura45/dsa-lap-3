# Agressive Cows ~ Interesting Pattern (Medium)
# Given: an array 'arr' of size 'n' which denotes the position/co-ordinates of stalls, an integer 'k' which denotes the number of aggressive cows.
# Task is to assign stalls to 'k' cows such that the minimum distance between any two of them is the maximum possible. 
# Find the max(min) distance between cows.

class Solution:

    # helper function
    def canPlaceCowsAtDistance(self, arr:list[int], k:int, dist:int)-> bool:
        lastPlaced = arr[0]
        cowsPlaced = 1
        for i in range(1,len(arr)):
            if arr[i] - lastPlaced >= dist:
                cowsPlaced += 1
                lastPlaced = arr[i]

        if cowsPlaced >= k:
            return True
        
        return False

    # brute
    def agressiveCows(self, arr:list[int], k:int) -> int:
        ans = -1
        arr.sort()

        # what can be the range of answer possible (1 -> max - min)
        low, high = 1, arr[-1] - arr[0]

        for d in range(low, high+1):
            if self.canPlaceCowsAtDistance(arr,k,d):
                ans = d

            else:
                break

        return ans

    # optimal
    def agressiveCows2(self, arr:list[int], k:int) -> int:
        ans = -1
        arr.sort()

        # what can be the range of answer possible (1 -> max - min)
        low, high = 1, arr[-1] - arr[0]

        while low<=high:
            mid = (low + high) //2

            if self.canPlaceCowsAtDistance(arr,k,mid):
                ans = mid
                low = mid + 1

            else:
                high = mid - 1

        return ans

if __name__=="__main__":
    stalls = list(map(int, input().split()))   # arr
    cows = int(input())                        # k

    sol = Solution()

    # res = sol.agressiveCows(stalls,cows)
    res = sol.agressiveCows2(stalls,cows)

    print(f"Maximum Possible Minimum Distance between {cows} Agressive Cows: {res}")