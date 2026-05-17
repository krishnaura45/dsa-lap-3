# Maximum consecutive number of 1's in a binary array

class Solution:
    # brute force ~ Takes too much time as it checks for every element and counts consecutive ones starting from that element
    def maxConsOnes_brute(self, nums:list)-> int:
        maxi = 0
        n = len(nums)
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == 1:
                    cnt += 1
                else:
                    break
            if cnt > maxi:
                maxi = cnt
        return maxi
    # TC ~ O(N^2), SC ~ O(1)

    # optimal ~ Using a single pass to count consecutive ones and keep track of the maximum count
    def maxConsOnes(self, nums:list)-> int:
        cnt,maxi = 0,0
        for i in nums:
            if i==1:
                cnt+=1
                if cnt>maxi: 
                    maxi=cnt
            else:
                cnt=0
        
        return maxi
    # TC ~ O(N), SC ~ O(1)
    
if __name__=="__main__":
    sol = Solution()
    arr = list(map(int, input().split()))
    # res = sol.maxConsOnes_brute(arr)
    res = sol.maxConsOnes(arr)
    print(f"Maximum consecutive ones: {res}")