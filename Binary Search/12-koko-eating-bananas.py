# Koko Eating Bananas

import math
class Solution:
    # Brute
    def minEatingSpeed(self, piles:list[int], h:int) -> int:

        for s in range(1,max(piles)+1):

            # caluculating total hours to finish bananas at rate 's'
            totalH = 0
            for pile in piles:
                totalH += math.ceil(pile / s)

            # as soon as we get the minimum integer 's' --> return it
            if totalH<=h:
                return s
            
        return -1
    # TC ~ O(maxPile * n)

    # Optimal
    def calculateTime(self, piles, speed):
        totalH = 0
        for pile in piles:
            totalH += math.ceil(pile / speed)

        return totalH
        

    def minEatingSpeed2(self, piles:list[int], h:int) -> int:
        low, high = 1, max(piles)

        # Binary search on answer space
        while low <= high:
            mid = (low + high) // 2

            totalH = self.calculateTime(piles, mid)

            if totalH <= h:
                # probably we got an answer but look yet for smallest
                high = mid - 1

            else:
                low = mid + 1

        return low
    # TC ~ O(n * log(maxPile))
    

if __name__=="__main__":
    arr = list(map(int,input().split()))
    h = int(input())

    sol = Solution()

    # res = sol.minEatingSpeed(arr,h)
    res = sol.minEatingSpeed2(arr,h)

    print(f"Minimum Rate for KOKO to eat all bananas: {res} bananas/hr")