# Minimum number of days to make M bouques
# where k adjacent flowers required to make 1 bouque

class Solution:
    # Brute Force
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)
        minDay, maxDay = min(bloomDay), max(bloomDay)

        for d in range(minDay,maxDay+1):
            b = 0     # to count the number of bouques which can be formed within d days
            cnt = 0   # to count consecutive flowers
            for i in bloomDay:
                if i<=d:
                    cnt += 1
                
                elif i>d:
                    b += (cnt//k)
                    cnt = 0

            # update b for the last change in count (understand by DRY RUN)
            b += (cnt//k)

            if b>=m:
                return d
            
        # otherwise if m*k>n
        return -1
    # TC ~ O((max-min+1)*n)
    
    # Optimal
    def possibleDay(self, arr, d, m, k):
        b = 0     # to count the number of bouques which can be formed within 'd' days
        cnt = 0   # to count consecutive flowers

        for i in arr:
            if i<=d:
                cnt += 1
            
            elif i>d:
                b += (cnt//k)
                cnt = 0

        # update b for the last change in count (understand by DRY RUN)
        b += (cnt//k)

        return (b>=m)

    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        low, high = min(bloomDay), max(bloomDay)
        ans = -1

        while low<=high:
            mid = (low + high) // 2

            if self.possibleDay(bloomDay,mid,m,k):
                ans = mid
                
                # try to look for smaller values
                high = mid - 1

            else:
                # eliminate left side
                low = mid + 1
            
        # otherwise if m*k > len(bloomDay)
        return ans
    # TC ~ O(n log(max-min+1))


if __name__=="__main__":
    arr = list(map(int,input().split()))
    m = int(input())
    k = int(input())

    sol = Solution()

    # res = sol.minDays(arr,m,k)
    res = sol.minDays2(arr,m,k)

    print(f"Minimum Days requied to make {m} bouques: {res}")