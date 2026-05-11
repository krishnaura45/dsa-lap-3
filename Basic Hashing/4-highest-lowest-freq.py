# Find highest and lowest frequency element
from collections import Counter
class Solution:
    def track_frequency(self, arr:list)-> None:
        freq = Counter(arr)

        maxf,minf=0,len(arr)
        max_el,min_el=0,0
        for i in range(len(arr)):
            count = freq[arr[i]]
            el = arr[i]

            if count > maxf:
                max_el = el
                maxf = count

            if count < minf:
                min_el = el
                minf = count

        print(f"Highest frequency element with freq {maxf} is {max_el}")
        print(f"Lowest frequency element with freq {minf} is {min_el}")

if __name__=="__main__":
    sol=Solution()
    L = list(map(int, input().split()))
    sol.track_frequency(L)