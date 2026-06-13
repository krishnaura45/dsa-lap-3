# Merge Overlapping sub-intervals

class Solution:
    # Brute Force
    def mergeOverlaps(self, intervals: list[list[int]])-> list[list[int]]:
        res = []
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])  # sort the intervals by their start element

        for i in range(n):
            start = intervals[i][0]
            end = intervals[i][1]

            # Skip all merged intervals
            if res and end <= res[-1][1]:
                continue

            # check the rest of the intervals for an overlap with the current interval
            for j in range(i+1, n):
                if intervals[j][0] <= end:
                    end = max(end, intervals[j][1])

                else:
                    break

            res.append([start, end])
        return res
    # TC ~ O(nlogn) + O(2n), SC ~ O(n) 
    
    # Optimal
    def mergeOverlaps2(self, intervals: list[list[int]])-> list[list[int]]:
        # sort the intervals by their start time
        intervals.sort(key=lambda x: x[0])
        ans = []

        for interval in intervals:
            # if the merged list is empty or the current interval does not overlap with the previous one, simply append it.
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                # otherwise, there is an overlap, so we merge the current and previous intervals by updating the end time of the previous interval if needed.
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans
    # TC ~ O(nlogn) + O(n), SC ~ O(n)
    
if __name__=="__main__":
    intervals = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]

    obj = Solution()

    # res = obj.mergeOverlaps(intervals)
    res = obj.mergeOverlaps2(intervals)
    print(res)