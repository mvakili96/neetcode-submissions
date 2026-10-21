class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        start = intervals[0][0]
        end = intervals[0][1]
        output_final = []
        for i in range(len(intervals)):
            if intervals[i][0] <= end:
                end = max(end,intervals[i][1])
            else:
                output_final.append([start,end])                        
                start = intervals[i][0]
                end = intervals[i][1]
        
            if i == len(intervals)-1:
                output_final.append([start,end])

        return output_final



                
