# Remove duplicates in-place from sorted array
# --> Basically, modify the array and return the number of unique elements

# leetcode solution
class Solution:
    # brute force 
    # leetcode performance: optimal runtime ~ 0 ms (>100%), 20.43 MB (>78.73%)
    def removeDuplicates(self, nums: list) -> int:
        unique = set()
        for i in nums:
            unique.add(i)

        i=0
        for j in sorted(unique):
            nums[i] = j                # k-1 duplicate elements will be ignored
            i+=1

        return i
    
    # optimal
    # leetcode performance: memory efficient ~ 75 ms (>5.2%), 17.91 MB (>100%)
    def removeDuplicates2(self, nums: list) -> int:
        i = 0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                nums[i+1] = nums[j]
                i += 1
        return i+1

if __name__=="__main__":
    sol=Solution()
    arr=list(map(int, input().split()))
    result=sol.removeDuplicates(arr)
    # result=sol.removeDuplicates2(arr)
    print(result)