# Single Element in sorted array (Medium)

class Solution:
    # Brute ~ O(n)
    def singleNonDuplicate(self, nums: list[int]) -> int:
        n = len(nums)

        if n==1:
            return nums[0]
        
        for i in range(n):
            if i==0:
                if nums[i]!=nums[i+1]:
                    return nums[i]
            
            elif i==n-1:
                if nums[i]!=nums[i-1]:
                    return nums[i]
            
            else:
                if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                    return nums[i]
                
        return -1
        
    
    # Optimal ~ O(log n)
    def singleNonDuplicate2(self, nums: list[int]) -> int:
        n = len(nums)

        # Edge cases
        if n==1:
            return nums[0]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[-1]!=nums[-2]:
            return nums[-1]
        
        # Binary search on trimmed search space
        low, high = 1, n-2
        while low<=high:
            mid = (low + high)//2
            # sure shot answer
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            
            # if standing on left half and single element is on right half -- (even, odd)
            if (mid%2==1 and nums[mid]==nums[mid-1]) or (mid%2==0 and nums[mid]==nums[mid+1]):
                # eliminate left half
                low = mid + 1

            # if standing on right half and single element is on left half -- (odd, even)
            else:
                # eliminate right half
                high = mid - 1
            
        return -1

if __name__=="__main__":
    arr = list(map(int, input().split()))

    sol = Solution()
    # print(f"Single Element in array: {sol.singleNonDuplicate(arr)}")
    print(f"Single Element in array: {sol.singleNonDuplicate2(arr)}")