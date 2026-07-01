# Allocate Minimum Number of Pages

# Problem Statement: Given an array ‘arr of integer numbers, ‘ar[i]’ represents the number of pages in the ‘i-th’ book. There are a ‘m’ number of students, and the task is to allocate all the books to the students.
# Allocate books in such a way that:
# Each student gets at least one book.
# Each book should be allocated to only one student.
# Book allocation should be in a contiguous manner.
# You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum.

class Solution:
    def countStudentsGettingBooks(self, arr, pages):
        cnt = 1
        lastBookPages = arr[0]
        
        for i in range(1,len(arr)):
            if lastBookPages + arr[i] <= pages:
                lastBookPages += arr[i]

            else:
                cnt += 1
                lastBookPages = arr[i]

        return cnt

    # brute
    def allocateBooks(self, arr:list[int], m:int) -> int:
        if len(arr)<m:
            return -1
        
        # range of answers possible
        low, high = max(arr), sum(arr)

        for pages in range(low, high+1):
            if self.countStudentsGettingBooks(arr,pages) <= m:
                return pages
            
        return low
    
    # optimal
    def allocateBooks2(self, arr:list[int], m:int) -> int:
        if len(arr)<m:
            return -1
        
        # range of answers possible
        low, high = max(arr), sum(arr)

        while low<=high:
            mid = (low + high) //2
            students = self.countStudentsGettingBooks(arr,mid)
            if students > m:
                low = mid + 1

            else:
                high = mid - 1
            
        return low

if __name__ == "__main__":
    arr = list(map(int, input().split()))  # array of number of pages in corr book
    m = int(input())                       # no. of students

    sol = Solution()

    # res = sol.allocateBooks(arr,m)
    res = sol.allocateBooks2(arr,m)

    print(f"Minimum Possible Maximum Pages: {res}")