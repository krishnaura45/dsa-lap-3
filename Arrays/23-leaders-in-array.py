# Leaders in an array

# A Leader is an element which is greater to all elements on its right.

from cmath import inf
class Solution:
    # brute
    def leaders(self, nums:list[int]):
        n = len(nums)
        ans = []         # to stre the answer

        for i in range(n-1):
            # Linear search type strategy
            leader = True
            for j in range(i+1,n):
                if nums[j]>nums[i]:
                    # if any element on right is greater than current then its not a leader
                    leader = False

            if leader == True:
                ans.append(nums[i])
            
        # last element will always be the leader
        ans.append(nums[-1])

        return ans

    # optimal ~ using one pass
    def leaders2(self, nums:list[int]):
        n = len(nums)
        ans = []

        maxi = -inf
        for i in range(n-1,-1,-1):
            if nums[i]>maxi:
                ans.append(nums[i])

            maxi = max(maxi,nums[i])

        # reverse to keep original order
        ans[:] = ans[::-1]
        
        return ans

if __name__=="__main__":
    arr = list(map(int, input().split()))

    sol = Solution()

    # res = sol.leaders(arr)
    res = sol.leaders2(arr)

    print(F"Leaders: {res}")