# Re-arrange array elements by sign

# Variety 1: Given an array of positive and negative numbers, arrange them such that every positive number is followed by a negative number, alternately. The order of appearance should be maintained. 
# Note: The number of positive and negative numbers in the array will be equal.
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

# Variety 2: Rearrange by sign if the number of positive and negative numbers in the array are not equal. 
class Solution2:
    # optimal --> modified version of the previous vareity's brute force
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        pos = []
        neg = []

        for i in nums:
            if i>0:
                pos.append(i)
            else:
                neg.append(i)

        cp, cn = len(pos), len(neg)
        ind = 0

        if cp>cn:
            for i in range(cn):
                nums[2*i] = pos[i]
                nums[2*i+1] = neg[i]
            
            ind = 2*cn

            for i in range(cn,cp):
                nums[ind] = pos[i]
                ind+=1

        else:
            for i in range(cp):
                nums[2*i] = pos[i]
                nums[2*i+1] = neg[i]

            ind = 2*cp
            for i in range(cp,cn):
                nums[ind] = neg[i]
                ind+=1

        return nums

    # TC ~ O(2n), SC ~ O(n)


if __name__=="__main__":
    arr = list(map(int, input().split()))

    # sol = Solution()
    sol2 = Solution2()

    # print(sol.rearrangeArray(arr))
    # print(sol.rearrangeArray2(arr))

    print(sol2.rearrangeArray(arr))
