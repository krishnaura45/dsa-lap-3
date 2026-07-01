# Leetcode Variation ~ Agressive Cows --> Magnetic Force Between Two Balls (1552)

class Solution:
    # helper
    def canPlaceBalls(self, arr:list[int], m:int, dist:int) -> bool:
        ballsPlaced = 1
        lastPlaced = arr[0]
        
        for i in range(1,len(arr)):
            if arr[i] - lastPlaced >= dist:
                ballsPlaced += 1
                lastPlaced = arr[i]

            else:
                continue

        return (ballsPlaced>=m)
    
    # Brute
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()

        for d in range(1, max(position) - min(position) +1):
            if self.canPlaceBalls(position, m, d):
                continue

            else:
                return d-1

        return -1
    
    # Optimal
    def maxDistance2(self, position: list[int], m: int) -> int:
        ans = -1
        position.sort()

        low, high = 1, max(position) - min(position)
        while low <= high:
            mid = (low + high) // 2

            if self.canPlaceBalls(position, m, mid):
                ans = mid
                low = mid + 1

            else:
                high = mid - 1

        return ans
    
    
if __name__=="__main__":
    arr = list(map(int, input().split()))  # position array
    m = int(input())                       # no. of balls to be placed

    sol = Solution()

    # res = sol.maxDistance(arr,m)
    res = sol.maxDistance2(arr,m)

    print(f"Maximum Possible Minimum Distance between {m} Magnetic Balls: {res}")