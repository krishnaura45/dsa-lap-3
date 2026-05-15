# Intersection of two sorted arrays
# Problem: Given two sorted arrays, find their intersection. The intersection of two arrays is a list of elements that are common to both arrays.

from collections import Counter
class Solution:
    # brute force ~ Check for each element of the smaller array if it is present in the larger array or not
    def intersection(self, arr1:list, arr2:list):
        common = []

        if len(arr1) <= len(arr2):
            for num in arr1:
                if num in arr2:
                    common.append(num)

        else:
            for num in arr2:
                if num in arr1:
                    common.append(num)
        
        return sorted(common)
    # TC ~ O(n*m), where n and m are the lengths of arr1 and arr2 respectively
    # SC ~ O(min(n,m)) --> extra space taken to return the answer list, which can be at most the size of the smaller array

    # better approach ~ Using a hash map to store the frequency of elements in the smaller array
    def intersection2(self, arr1:list, arr2:list):
        common = []
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1
        freq = Counter(arr2)
        for num in arr1:
            if freq[num] > 0:
                common.append(num)
                freq[num] -= 1
        
        return common
    # TC ~ O(n + m), where n and m are the lengths of arr1 and arr2 respectively
    # SC ~ O(min(n,m)) --> extra space for the frequency map of the smaller array and the result list, both can be up to size min(n, m) in the worst case

    # optimal ~ Using two pointers since both arrays are sorted
    def intersection3(self, arr1:list, arr2:list):
        ans = []
        i,j = 0,0
        while i<len(arr1) and j<len(arr2):
            if arr1[i] == arr2[j]:
                ans.append(arr1[i])
                i+=1
                j+=1
            elif arr1[i] < arr2[j]:
                i+=1
            else:
                j+=1
        
        return ans
    # TC ~ O(n + m), where n and m are the lengths of arr1 and arr2 respectively
    # SC ~ O(min(n,m))

if __name__=="__main__":
    sol = Solution()
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # res = sol.intersection(a,b)
    # res = sol.intersection2(a,b)
    res = sol.intersection3(a,b)

    print(f"Intersection of two sorted arrays: {res}")