# Least Capacity to ship packages within D days

class Solution:
    def daysToShip(self, wts:list[int], cap:int) -> int:
        cntDay = 1
        load = 0
        for w in wts:
            if load + w > cap:
                cntDay += 1
                load = w

            else:
                load += w

        return cntDay

    # Brute
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        # to ship each wt, the minimum capacity of ship should be max(weights)
        # and maximum capacity can be sum of all weights

        for cap in range(max(weights),sum(weights)+1):
            # calculate how much days will it take to ship all weights
            daysReq = self.daysToShip(weights,cap)

            if daysReq <= days:
                return cap
            
        return -1

    # Optimal
    def shipWithinDays2(self, weights: list[int], days: int) -> int:
        # to ship each wt, the minimum capacity of ship should be max(weights)
        # and maximum capacity can be sum of all weights

        low, high = max(weights), sum(weights)

        while low<=high:

            mid = (low + high) // 2

            # calculate how much days will it take to ship all weights
            daysReq = self.daysToShip(weights,mid)

            # trimming conditions
            if daysReq <= days:
                # we need to eliminate the right side to look for any smaller capacity possible
                high = mid - 1

            else:
                low = mid + 1

        # at start, 'low' was pointing to 'not possible' answer --> after convergence, it will point to 'possible' answer
        return low


if __name__=="__main__":

    wts = list(map(int, input().split()))
    D = int(input())

    sol = Solution()

    # res = sol.shipWithinDays(wts,D)
    res = sol.shipWithinDays2(wts,D)

    print(f"Least capacity to ship packages within {D} days: {res}")