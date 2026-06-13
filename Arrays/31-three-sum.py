# 3 Sum problem --> Find all unique triplets such that target sum is equal to 0
# Medium - Hard

class Solution:
    
    # BRUTE FORCE
    # Fix first element, try every possible pair after it.
    # For each triplet:
    #   - Check if sum == 0
    #   - Sort triplet to handle permutations
    #   - Add only if not already present

    def threeSum(self, nums:list[int])-> list[list[int]]:
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
    # TC: O(n³), SC: O(1) excluding O(# unique triplets) to return answer

    # BETTER (Hashing)
    # Fix nums[i].
    # Reduce problem to finding Two Sum = -nums[i].
    # Use hashset to find third element in O(1).
    # Sort triplet before storing to avoid duplicate permutations.
    # Store triplets in a set for automatic duplicate removal.

    def threeSum2(self, nums:list[int])-> list[list[int]]:
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
    # TC: O(n² * log m), SC: O(n) + O(k) 
    # where m is variable for elements in hashset
    # and k is no. of unique triplets


    # OPTIMAL (Sorting + Two Pointers)
    # Step 1: Sort array.
    # Step 2: Fix nums[i].
    # Step 3: Use two pointers (j,k) to find remaining pair.
    #   sum < 0 -> move left pointer right
    #   sum > 0 -> move right pointer left
    #   sum == 0 -> store triplet and skip duplicates
    # Skip duplicate values of i to avoid repeated triplets.

    def threeSum3(self, nums:list[int])-> list[list[int]]:
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
    # TC ~ O(n²) + O(nlogn), SC ~ O(1) excluding output

if __name__ == "__main__":
    arr = list(map(int, input().split()))

    sol = Solution()

    # res = sol.threeSum(arr)
    # res = sol.threeSum2(arr)
    res = sol.threeSum3(arr)

    print(res)