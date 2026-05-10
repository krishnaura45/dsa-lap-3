# Basic set of problems in Recursion
# 1. Infinite Reecursion
# 2. Print name N times
# 3. Print 1 to N linearly (using Recursion & Backtracking)
# 4. Print N to 1 lineraly (using Recursion & Backtracking)
# 5. Sum of the first N natural numbers
# 6. Factorial of a number

class Solution:
    # probelem 1
    def infiniteRecursion(self):
        print(1)
        self.infiniteRecursion()

    # problem 2
    def printName(self, i:int, n:int)-> int:
        if i>n: return
        print("Krish")
        self.printName(i+1,n)

    # problem 3
    # using recursion
    def printSequence_r(self, i:int, n:int):
        if i>n: return
        print(i)
        self.printSequence_r(i+1,n)
    
    # using backtrack
    def printSequence_b(self, i:int, n:int):
        if i==0: return
        self.printSequence_b(i-1,n)
        print(i)
    
    # problem 4
    # using recursion
    def printRevSequence_r(self, i:int, n:int):
        if i<1: return
        print(i)
        self.printRevSequence_r(i-1,n)
    
    # using backtrack
    def printRevSequence_b(self, i:int, n:int):
        if i>n: return
        self.printRevSequence_b(i+1,n)
        print(i)
    
    # problem 5
    # parameterized approach
    def sum_param(self, i:int, s:int)-> int:
        if i==0: return s
        return self.sum_param(i-1,s+i)
    
    # functional approach --> simpler
    def sum_func(self, n: int)-> int:
        if n==1: return 1
        return n+self.sum_func(n-1)
    
    # problem 6
    # parameterized approach
    def factorial_p(self, i:int, product:int)-> int:
        if i==0: return product
        return self.factorial_p(i-1,product*i)
    
    # functional approach --> simpler
    def factorial_f(self, n: int)-> int:
        if n==0: return 1
        return n*self.factorial_f(n-1)
    
# main function
if __name__ == "__main__":
    sol = Solution()
    # res_1=sol.infiniteRecursion()  # stack overflow --> recursion error

    N=int(input())
    # res_2=sol.printName(1,N)

    # res_3=sol.printSequence_r(1,N)
    # res_4=sol.printSequence_b(N,N)

    # res_5=sol.printRevSequence_r(N,N)
    # res_6=sol.printRevSequence_b(1,N)

    # print(sol.sum_param(N,0))
    print(sol.sum_func(N))

    # print(sol.factorial_p(N,1))
    print(sol.factorial_f(N))