# Pascal's Triangle
# Variation 1: Given row number and column number, find the element at that place
class Solution_v1():
    # helper
    def ncr(self, n:int, r:int)-> int:
        res = 1
        for i in range(r):
            res *= (n-i)
            res //= (i+1)
        return res
    
    # actual
    def pascalElement(self, R:int, C:int)-> int:
        return self.ncr(R-1, C-1)
    
    # TC ~ O(R), SC ~ O(1)


# Variation 2: Print any Nth row of Pascal's triangle
class Solution_v2():
    # Extreme Brute
    def ncr(self, n:int, r:int)-> int:
        res = 1
        for i in range(r):
            res *= (n-i)
            res //= (i+1)
        return res
    
    def pascalRow(self, n:int)-> None:
        for c in range(1,n+1):
            print(self.ncr(n-1,c-1))

    # TC ~ O(n*r)

    # Optimal
    def pascalRow2(self, n:int)-> list[int]:
        ans = 1
        print(ans)
        for c in range(1,n):
            ans *= (n-c)
            ans //= c
            print(ans)

    # TC ~ O(n)

# Variation 3: Given N, print the entire pascal's triangle upto row N
class Solution_v3():
    # Naive ~ using ncr for elements of each row --> O(n*n*r)

    # Optimal
    def generateRow(self, n:int)-> list[int]:
        row = []
        ans = 1
        row.append(ans)
        for c in range(1,n):
            ans *= (n-c)
            ans //= c
            row.append(ans)

        return row
    
    def pascalTriangle(self, n:int)-> list[list[int]]:
        ans = []
        for row in range(1,n+1):
            ans.append(self.generateRow(row))

        return ans
    
    # TC ~ O(n^2)

if __name__ == "__main__":
    # sol = Solution_v1()
    # R, C = list(map(int, input().split()))
    # print(sol.pascalElement(R,C))

    # sol = Solution_v2()
    # N = int(input())
    # sol.pascalRow(N)
    # sol.pascalRow2(N)

    sol = Solution_v3()
    N = int(input())
    print(sol.pascalTriangle(N))