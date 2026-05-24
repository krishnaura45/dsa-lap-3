# Reverse string
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    # using two pointer
    def reverse1(self, s: list[str]) -> None:
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return s
    # can even reverse any sub-string

    # using one pointer
    def reverse2(self, s: list[str]) -> None:
        n = len(s)
        i = 0

        while i < n - i - 1:
            s[i], s[n - i - 1] = s[n - i - 1], s[i]
            i += 1

        return s
    
if __name__ == "__main__":
    s = list(input())
    sol = Solution()
    print(sol.reverse1(s))
    # print(sol.reverse2(s))