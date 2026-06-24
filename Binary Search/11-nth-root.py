# Nth root of an Integer (if exists)

class Solution:
    # Brute
    def findRoot(self, i:int, n:int) -> int:
        ans = -1

        for x in range(1,n+1):
            if x**n == i:
                ans = x

            elif x**n > i:
                break
        
        return ans
    # TC ~ O(m log n)

    # Optimal
    def findRoot2(self, i:int, n:int) -> int:
        low, high = 1, i
        
        while low <= high:
            mid = (low + high) // 2

            if mid**n == i:
                # answer
                return  mid

            elif mid**n < i:
                low = mid + 1

            else:
                high = mid - 1

        return -1
    # TC ~ O(log m * log n)

    # Optimal 2
    def findRoot3(self, i:int, n:int):
        # Set low and high for binary search
        low, high = 1, i

        # Start binary search
        while low <= high:
            # Calculate mid
            mid = (low + high) // 2

            # Store result of mid^n
            ans = 1
            for _ in range(n):
                ans *= mid
                if ans > i:
                    break

            # If mid^n equals m
            if ans == i:
                return mid

            # If mid^n is less than m
            if ans < i:
                low = mid + 1

            # If mid^n is more than m
            else:
                high = mid - 1

        # Return -1 if not found
        return -1
    

if __name__=="__main__":
    num = int(input())
    n = int(input())

    sol = Solution()
    # res = sol.findRoot(num,n)
    # res = sol.findRoot2(num,n)
    res = sol.findRoot3(num,n)

    if res!=-1:
        print(f"{n}th Root of {num}: {res}")
    else:
        print(f"{n}th root of {num} does not exist")