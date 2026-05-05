# Greatest Common Divisor (GCD) of two numbers
# brute force ~ O(min(a,b))
class Solution:
    def gcd(self, a: int, b: int)-> int:
        cf=1
        for i in range(1,min([a,b])+1):
            if a%i==0 and b%i==0:
                cf=i
        return cf

class Solution2:
    def gcd(self, a: int, b: int)-> int:
        hcf=1
        for i in range(min([a,b]),1,-1):
            if a%i==0 and b%i==0:
                hcf=i
                break
        return hcf
    
# optimal
# Euclidean Algorithm --> gcd(a,b) = gcd(a-b,b) if a>b
class Solution3:
    def gcd(self, a: int, b: int)-> int:
        while a>0 and b>0:
            if a>b:
                a=a-b
            else:
                b=b-a
        if a==0: return b
        else: return a

# Updated Euclidean Algorithm --> gcd(a,b) = gcd(a%b,b) if a>b
class Solution4:
    def gcd(self, a: int, b: int)-> int:
        while a>0 and b>0:
            if a>b:
                a=a%b
            else:
                b=b%a
        if a==0: return b
        else: return a
# TC ~ O(log (min(a,b))) , log base=phi
    
if __name__ == "__main__":
    sol = Solution3()
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    res = sol.gcd(a,b)
    print(f"HCF of {a} and {b}:",res)