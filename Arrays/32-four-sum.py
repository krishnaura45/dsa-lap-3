# 4 Sum problem --> Find all unique quadruplets such that target sum is equal to 0
# Medium - Hard

class Solution:
    
    # BRUTE FORCE
    def fourSum(self, nums:list[int])-> list[list[int]]:
        n = len(nums)
        ans = []

        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    triplet = []
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]

                        triplet.sort()
                        if triplet not in ans:
                            ans.append(triplet)

        return ans

    # BETTER
    def fourSum2(self, nums:list[int])-> list[list[int]]:
        n = len(nums)
        triplets_st = set()

        for i in range(n):
            hashset = set()

            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])

                if third in hashset:
                    temp = tuple(sorted((nums[i], nums[j], third)))
                    triplets_st.add(temp)

                hashset.add(nums[j])

        return [list(triplet) for triplet in triplets_st]


    # OPTIMAL
    def fourSum3(self, nums:list[int])-> list[list[int]]:
        n = len(nums)
        ans = []
        nums.sort()

        for i in range(n):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                triplet_sum = nums[i] + nums[j] + nums[k]

                if triplet_sum < 0:
                    j += 1

                elif triplet_sum > 0:
                    k -= 1

                else:
                    ans.append([nums[i], nums[j], nums[k]])

                    # Move both pointers after finding valid triplet
                    j += 1
                    k -= 1

                    # Skip duplicate second elements
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    # Skip duplicate third elements
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

        return ans
    

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    sol = Solution()

    # res = sol.fourSum(arr)
    # res = sol.fourSum2(arr)
    res = sol.fourSum3(arr)

    print(res)