# Check Pallindrome number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            return x==int(str(x)[::-1])
# runtime ~ 11 ms (>37.0%) | memory ~ 19.3 MB (>18.78%)
        
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if str(x)[::-1]==str(x):
            return True
        else:
            return False
# runtime ~ 0 ms (>100%) | memory ~ 19.22 MB (>54.08%)
    
# driver
if __name__ == "__main__":
    sol = Solution2()
    # N=int(input("Enter a number: "))
    N1=329823   # 121, 7887, 23523
    flag = sol.isPalindrome(N1)
    if flag==True: print(f" {N1} is Pallindrome")
    else: print(f" {N1} is not a Pallindrome")