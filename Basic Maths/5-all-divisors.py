# Print all divisors/factors of a number
# brute force ~ O(n), O(n)
class Solution:
    def printDivisors(self, n: int) -> None:
        L=[]
        for i in range(1,n+1):
            if n%i==0:
                L.append(i)
        print(f"Divisors of {n}: ",L)
     
# better ~ O(sqrt(n)), O(2*sqrt(n))
import math
class Solution2:
    def printDivisors(self, n: int) -> None:
        L=[]
        # going upto sqrt(n) using math module
        for i in range(1,int(math.sqrt(n))+1):
            if n%i==0:
                L.append(i)
                if i!=n/i: L.append(int(n/i))
        print(f"Divisors of {n}: ",L)

# optimal ~ O(sqrt(n)), O(2*sqrt(n))
class Solution3:
    def printDivisors(self, n: int) -> None:
        L=[]
        i=1
        # going upto sqrt(n) and saving runtime
        while i**2<=n:
            if n%i==0:
                L.append(i)
                if i!=n//i: L.append(n//i)
            i+=1
        L.sort()
        print(f"Divisors of {n}: ",L)
    
# driver
if __name__ == "__main__":
    sol = Solution3()
    N=int(input("Enter a number: "))
    res = sol.printDivisors(N)