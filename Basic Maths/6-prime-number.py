# Check Prime number
# brute force ~ O(n)
class Solution:
    def isPrime(self, n: int) -> bool:
        # counter variable for counting no. of factors
        c=0
        for i in range(1,n+1):
            if n%i==0: c+=1
        return c==2

        
# optimal ~ O(sqrt(n))
class Solution2:
    def isPrime(self, n: int) -> bool:
        c,i=0,1
        while i*i<=n:
            if n%i==0:
                c+=1
                if i!=n//i:
                    c+=1
            i+=1
        return c==2
    
# driver
if __name__ == "__main__":
    sol = Solution2()
    N=int(input("Enter a number: "))
    flag = sol.isPrime(N)
    if flag==True: print(f" {N} is Prime")
    else: print(f" {N} is not a Prime")