# Square Root of an Integer
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

class Solution:
    # Brute
    def findsqrt(self, n:int) -> int:
        ans = -1

        for x in range(1,n+1):
            if x**2<=n:
                ans = x

            else:
                break
        
        return ans
    

    # Optimal
    def findsqrt2(self, n:int) -> int:
        low, high = 1, n
        
        while low <= high:
            mid = (low + high) // 2

            if mid**2 <= n:
                # may be an answer
                # ans = mid

                # but we'll look on the right to get the nearest integer
                low = mid + 1

            else:
                # if square of mid > n then it is definitely not an answer
                # thereby eliminate right half
                high = mid - 1

        # eventually high will be pointing to the ANSWER
        return high
    

if __name__=="__main__":
    n = int(input())

    sol = Solution()
    # print(f"Rounded Square Root of {n}: {sol.findsqrt(n)}")
    print(f"Rounded Square Root of {n}: {sol.findsqrt2(n)}")
