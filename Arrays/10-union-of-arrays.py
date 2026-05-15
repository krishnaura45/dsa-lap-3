# Union of two sorted arrays
# Problem: Given two sorted arrays, find their union. The union of two arrays is the set of elements that are present in either of the two arrays. 
# The union should not contain duplicate elements.

class Solution:
    # brute force 
    def union(self, arr1:list, arr2:list):
        # Using a set to store unique elements
        union_set = set()
        
        # Add elements from both arrays
        for num in arr1:
            union_set.add(num)
        for num in arr2:
            union_set.add(num)
        
        # Convert set to list and sort it
        union_list = sorted(list(union_set))
        return union_list
    
    # TC, SC ~ O(n log n + m log m), O(n + m) where n and m are the lengths of arr1 and arr2 respectively

    # optimal ~ Using two pointers
    def union2(self, arr1:list, arr2:list):
        i, j = 0, 0
        union = []

        while i < len(arr1) and j < len(arr2):
            # Compare elements of both arrays and add the smaller one to the union
            # Also, to ensure that we do not add duplicates to the union
            if arr1[i] < arr2[j] and (len(union) == 0 or union[-1] != arr1[i]):
                union.append(arr1[i])
                i += 1
            
            elif arr1[i] > arr2[j] and (len(union) == 0 or union[-1] != arr2[j]):
                union.append(arr2[j])
                j += 1
            
            # If both elements are equal, add it once and move both pointers
            else:
                if len(union) == 0 or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
                j += 1

        # Append any remaining elements from either array
        while i < len(arr1):
            if len(union) == 0 or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1

        while j < len(arr2):
            if len(union) == 0 or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

        return union
    # TC, SC ~ O(n + m), O(n + m) where n and m are the lengths of arr1 and arr2 respectively
        
if __name__=="__main__":
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    sol = Solution()
    # union = sol.union(arr1, arr2)
    union = sol.union2(arr1, arr2)
    print(f"Union of the two arrays: {union}")