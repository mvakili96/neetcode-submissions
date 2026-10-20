class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals

        s = newInterval[0]
        if s >= intervals[-1][0]:
            intervals.append(newInterval)
        elif s <= intervals[0][0]:
            intervals.insert(0,newInterval)
        else:
            for i in range(len(intervals)-1):
                if s >= intervals[i][0] and s <= intervals[i+1][0]:
                    intervals.insert(i+1,newInterval)
                    break
        
        i = 0
        while i < len(intervals)-1:
            if intervals[i+1][0] <= intervals[i][1]:
                intervals.insert(i+2,[intervals[i][0],max(intervals[i][1],intervals[i+1][1])])
                intervals.pop(i+1)
                intervals.pop(i)
                continue
            i += 1

        return intervals

        