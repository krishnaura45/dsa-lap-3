# Check Armstrong number
# Given an integer n, return true if and only if it is an Armstrong number.
# The k-digit number n is an Armstrong number if and only if the kth power of each digit sums to n.
# brute ~ O(2 log x)
class Solution:
    def isArmstrong(self, x: int) -> bool:
        a,b=x,x
        sum=0
        cnt=0
        while a>0:
            d=a%10
            a=a//10
            cnt+=1
        while b>0:
            d=b%10
            b=b//10
            sum+=d**cnt
        if sum==x:
            return True
        return False

# optimal ~ O(log n)        
class Solution2:
    def isArmstrong(self, n: int) -> bool:
        k = len(str(n))
        s, x = 0, n
        while x:
            s += (x % 10) ** k
            x //= 10
        return s == n
    
# driver
if __name__ == "__main__":
    sol = Solution2()
    N=int(input("Enter a number: "))
    # N=153, 371, 1634, 123
    flag = sol.isArmstrong(N)
    if flag==True: print(f" {N} is an Armstrong number")
    else: print(f" {N} is not an Armstrong")