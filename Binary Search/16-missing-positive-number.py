# K th Missing positive number (starting from 1)

class Solution:
    # Brute ~ O(n^2)
    def findKthPositive(self, nums: list[int], k: int) -> int:
        missing = 0
        for el in range(1,nums[-1]+k+1):
            if el not in nums:
                missing+=1

            if missing == k:
                return el

        return -1

    # Better ~ O(n)
    def findKthPositive2(self, nums: list[int], k: int) -> int:
        for x in nums:
            if x <= k:
                k += 1

            else:
                break
        
        return k
    
    # Optimal ~ O(log n)
    def findKthPositive3(self, arr: list[int], k: int) -> int:
        low, high = 0, len(arr)-1

        while low<=high:
            mid = (low + high) // 2

            # figure out the number of missing numbers till 'mid' index
            missing = arr[mid] - (mid + 1)

            # somehow figuring out the interval (two nearby indexes) where kth missing positive number should be present
            if missing <= k:
                low = mid + 1

            else:
                high = mid - 1
        return high + k + 1       # low + k

if __name__=="__main__":

    arr = list(map(int, input().split()))
    k = int(input())

    sol = Solution()

    # res = sol.findKthPositive(arr,k)
    # res = sol.findKthPositive2(arr,k)
    res = sol.findKthPositive3(arr,k)

    print(f"{k}th missing positive number: {res}")