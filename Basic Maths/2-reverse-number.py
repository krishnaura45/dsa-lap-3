# Reverse a number
class Solution:
    def reverseNum(self, n: int)-> int:
        rev=0
        a=n
        while(a>0):
            d=a%10
            a=a//10
            rev=(rev*10)+d
        return rev

class Solution2:
    def reverseNum(self, n: int)-> int:
        s=str(n)
        s=s[::-1]
        rev=int(s)
        return rev


# Modification (Leet code type)
# Reverse an Integer ~ can handle +/- numbers easily
class Solution3:
    def reverseNum(self, n: int)-> int:
        rev=0
        a=n
        if n>=0:
            rev = int(str(a)[::-1])
        else:
            rev = int(str(n)[1:][::-1])*-1
        if rev<-2**31 or rev>2**31-1:
            return 0
        return rev
    
# driver
if __name__ == "__main__":
    sol = Solution2()
    # N=int(input("Enter a number: "))
    N1=329823
    digits = sol.reverseNum(N1)
    print(f"Reverse of Number {N1}:",digits)

    opt = Solution3()
    # N=int(input("Enter a number: "))
    N2=-731
    digits = opt.reverseNum(N2)
    print(f"Reverse of Number {N2}:",digits)