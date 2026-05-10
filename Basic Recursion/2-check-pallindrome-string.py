# Check if a single string is pallindrome or not
# using recursion
class Solution:
    def palindrome(self, i:int, s: str):
        s=s.lower()
        n=len(s)
        if i>=n//2:
            return True
        if s[i]!=s[n-i-1]:
            return False
        return self.palindrome(i+1,s)

# without recursion
class Solution2:
    def palindrome(self, s: str):
        s=s.lower()
        n=len(s)
        i=0
        while i<=n//2:
            if s[i]!=s[n-i-1]:
                return False
            i+=1
        return True

# Leetcode solution ~ Valid Pallindrome Phrase
class Solution3:
    def isPalindrome(self, s: str):
        s=s.lower()
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i] != s[j]:
                return False
            else:
                i, j = i + 1, j - 1
        return True

if __name__== "__main__":
    s=input()
    # sol=Solution()
    # flag=sol.palindrome(0,s)
    # sol=Solution2()
    # flag=sol.palindrome(s)
    sol=Solution3()
    flag=sol.isPalindrome(s)
    if flag==1: print(f"'{s}' is pallindrome")
    else: print(f"'{s}' is not pallindrome")