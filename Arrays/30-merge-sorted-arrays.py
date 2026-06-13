# Merge two sorted arrays

class Solution:
    def mergeSortedArrays(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        m, n = len(nums1), len(nums2)
        i, j = 0, 0

        while i<m and j<n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i+=1

            else:
                res.append(nums2[j])
                j+=1

        while i<m:
            res.append(nums1[i])
            i+=1

        while j<n:
            res.append(nums2[j])
            j+=1

        for i in range(m+n):
            if i<m:
                nums1[i] = res[i]
            else:
                nums2[i-m] = res[i]

        return nums1 + nums2
    # TC ~ O(m+n) + O(m+n), SC ~ O(m+n)

    # Optimal 1
    def mergeSortedArrays2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        m, n = len(nums1), len(nums2)
        left = m-1
        right = 0

        while left>=0 and right<n:
            if nums1[left] > nums2[right]:
                # perform swap
                nums1[left], nums2[right] = nums2[right], nums1[left]
                left-=1
                right+=1

            else:
                break

        # sort both arrays
        nums1.sort()
        nums2.sort()

        return nums1 + nums2
    # TC ~ O(min(m,n)) + O(mlogm) + O(nlogn), SC ~ O(1)

    # Optimal 2 ~ gap method
    def mergeSortedArrays2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        m, n = len(nums1), len(nums2)
        
        return nums1 + nums2

if __name__=="__main__":
    sol = Solution()

    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    # res = sol.mergeSortedArrays(arr1, arr2)
    res = sol.mergeSortedArrays2(arr1, arr2)
    # res = sol.mergeSortedArrays3(arr1, arr2)

    print(res)


# ----> Leetcode variation ~ modified solutions at LC