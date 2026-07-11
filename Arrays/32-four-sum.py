# 4 Sum problem --> Find all unique quadruplets such that target sum is achieved
# Medium - Hard

class Solution:
    
    # BRUTE FORCE
    def fourSum(self, nums:list[int], target:int)-> list[list[int]]:
        n = len(nums)
        st = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            temp = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
                            st.add(temp)

        return [list(quad) for quad in st]

    # BETTER
    def fourSum2(self, nums:list[int], target:int)-> list[list[int]]:
        n = len(nums)
        st = set()

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()  # Store numbers between j and k
                for k in range(j + 1, n):
                    required = target - nums[i] - nums[j] - nums[k]

                    if required in seen:
                        temp = tuple(sorted([nums[i], nums[j], nums[k], required]))
                        st.add(temp)

                    seen.add(nums[k])

        return [list(quad) for quad in st]


    # OPTIMAL
    def fourSum3(self, arr:list[int], target:int)-> list[list[int]]:
        n = len(arr)
        arr.sort()
        ans = []

        for i in range(n):
            if i > 0 and arr[i] == arr[i - 1]:
                continue

            for j in range(i + 1, n):
                if j > i + 1 and arr[j] == arr[j - 1]:
                    continue

                left, right = j + 1, n - 1
                while left < right:
                    total = arr[i] + arr[j] + arr[left] + arr[right]

                    if total == target:
                        ans.append([arr[i], arr[j], arr[left], arr[right]])

                        while left < right and arr[left] == arr[left + 1]:
                            left += 1
                        while left < right and arr[right] == arr[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return ans
    

if __name__ == "__main__":
    arr = list(map(int, input().split()))
    target = int(input())

    sol = Solution()

    # res = sol.fourSum(arr,target)
    # res = sol.fourSum2(arr,target)
    res = sol.fourSum3(arr,target)

    print(res)
