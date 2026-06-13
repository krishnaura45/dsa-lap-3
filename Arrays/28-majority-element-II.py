# Majority Element - II
# Given an array of size n, find the element/s that appear more than ⌊ n/3 ⌋ times.

from collections import Counter
class Solution:
  # brute force
    def majorityElement(self, nums:list[int]) -> list[int]:
        n = len(nums)
        ans = []
        for i in range(n):
            cnt = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    cnt+=1
            
            if nums[i] not in ans and cnt > n//3:
                ans.append(nums[i])

        return ans
    # TC ~ O(n^2), SC ~ O(1)

    # better ~ hashmap
    def majorityElement2(self, nums:list[int]) -> list[int]:
        freq = Counter(nums)
        ans = []
        for key, value in freq.items():
            if value > len(nums)//3:
                ans.append(key)
            
        return ans
    # TC ~ O(2n), SC ~ O(n)

    def majorityElement3(self, nums:list[int]) -> list[int]:
        mpp = {}
        ans = []
        minf = len(nums)//3 + 1

        for e in nums:
            if e not in mpp:
                mpp[e] = 1
            else:
                mpp[e] += 1

            if mpp[e] == minf:
                ans.append(e)

            if len(ans) == 2:
                break
            
        return ans
    # TC ~ O(n), SC ~ O(n)

    def majorityElement4(self, nums:list[int]) -> list[int]:
        ans = []
        count1, count2 = 0, 0
        el1, el2 = float('-inf'), float('-inf')

        for i in nums:
            if count1==0 and i!=el2:
                count1 = 1
                el1 = i

            elif count2==0 and i!=el1:
                count2 = 1
                el2 = i

            elif i == el1:
                count1 += 1

            elif i == el2:
                count2 += 1

            else:
                count1 -= 1
                count2 -= 1
        
        # verify if el is the majority element
        cnt1, cnt2 = 0, 0
        for i in nums:
            if i == el1:
                cnt1 += 1
            if i == el2:
                cnt2 += 1 
        
        minf = len(nums)//3 + 1
        if cnt1 >= minf:
            ans.append(el1)

        if cnt2 >= minf and el1 != el2:
            ans.append(el2)

        return ans
    # TC ~ O(2n), SC ~ O(1)

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    sol = Solution()

    # print(sol.majorityElement(arr))
    # print(sol.majorityElement2(arr))
    # print(sol.majorityElement3(arr))
    print(sol.majorityElement4(arr))