# Re-arrange array elements by sign

class Solution:
    # brute force
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pos = []
        neg = []

        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)

        for i in range(n//2):
            nums[2*i] = pos[i]
            nums[2*i + 1] = neg[i]

        return nums
    # TC ~ O(2n), SC ~ O(n)
    
    # optimal ~ two pointer approach
    def rearrangeArray2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0]*n
        posIndex, negIndex = 0, 1
        for i in nums:
            if i > 0:
                res[posIndex] = i
                posIndex += 2
            else:
                res[negIndex] = i
                negIndex += 2
        
        return res
    # TC ~ O(n), SC ~ O(1)

if __name__=="__main__":
    pass