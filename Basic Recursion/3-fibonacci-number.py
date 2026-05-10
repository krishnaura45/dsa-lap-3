# Fibonacci Number upto nth term (0 based indexing)
class Solution:
    # without recursion
    def fibo1(self, n:int)-> int:
        a,b=0,1
        for _ in range(n):
            a,b=b,a+b
        return a
    
    # using recursion -> multiple calls
    def fibo2(self,n:int)-> int:
        if n<=1: return n
        return self.fibo2(n-1)+self.fibo2(n-2)

if __name__=="__main__":
    N=int(input())
    sol=Solution()
    # print(f"Fibonacci Series term {N}: ",sol.fibo1(N))
    print(f"Fibonacci Series term {N}: ",sol.fibo2(N))