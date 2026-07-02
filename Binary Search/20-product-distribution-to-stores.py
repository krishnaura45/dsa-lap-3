# Leetcode 2064 - Minimized Maximum of Products Distributed to any store

# You are given an integer n indicating there are n specialty retail stores. There are m product types of varying amounts, which are given as a 0-indexed integer array quantities, where quantities[i] represents the number of products of the ith product type.
# You need to distribute all products to the retail stores following these rules:

# A store can only be given at most one product type but can be given any amount of it.
# After distribution, each store will have been given some number of products (possibly 0). Let x represent the maximum number of products given to any store. You want x to be as small as possible, i.e., you want to minimize the maximum number of products that are given to any store.
# Return the minimum possible x.

class Solution:
    # brute
    def distributeProducts(self, k: int, quantities: list[int]) -> int:
        for x in range(1, max(quantities) + 1):

            stores = 0
            for q in quantities:
                stores += (q + x - 1) // x

            if stores <= k:
                return x
            

    # optimal
    def countStoresByQuantityLimit(self, quantities: list[int], lim:int) -> int:
        cnt = 0

        for q in quantities:
            cnt += (q + lim - 1) // lim

        return cnt

    def distributeProducts2(self, k: int, quantities: list[int]) -> int:
        low = 1
        high = max(quantities)

        while low <= high:
            mid = (low + high) // 2

            stores = self.countStoresByQuantityLimit(quantities,mid)
            if stores <= k:
                high = mid - 1

            else:
                low = mid + 1

        return low
            

if __name__ == "__main__":
    k = int(input())
    arr = list(map(int, input().split()))

    sol = Solution()

    # res = sol.distributeProducts(k,arr)
    res = sol.distributeProducts2(k,arr)

    print(f"Minimized Maximum Quantity of Products: {res}")