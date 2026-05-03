# Count all digits of a number
# Brute Force
class Solution:
    def countDigits(self, N: int)-> int:
        a=N
        counter=0
        while(a>0):
            d=a%10
            a=a//10
            counter+=1
        return counter

# Optimal
import math
class Solution2:
    def countDigits(self, n: int)-> int:
        cnt = int(math.log10(n) + 1)   # Adding 1 to the result accounts for the case when 'n' is a power of 10, ensuring that the count is correct.
        return cnt

if __name__ == "__main__":
    sol = Solution2()
    N=int(input("Enter a number: "))
    digits = sol.countDigits(N)
    print(f"Number of digits in {N}:",digits)