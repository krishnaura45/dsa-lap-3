class Solution:
    # iterative
    def binarySearch(self, nums:list[int], x:int)-> int:
        n = len(nums)
        low, high = 0, n-1
        ans = -1

        while low<=high:
            mid = (low + high) // 2
            if nums[mid] == x:
                ans = mid
                break

            elif nums[mid] < x:
                low = mid + 1

            else:
                high = mid - 1
        
        return ans
    
    # recursive
    
if __name__=="__main__":
    arr = list(map(int, input().split()))
    num = int(input())

    sol = Solution()

    res = sol.binarySearch(arr, num)

    if res>=0:
        print(f"Element present at index {res}")
    else:
        print("Element not present")