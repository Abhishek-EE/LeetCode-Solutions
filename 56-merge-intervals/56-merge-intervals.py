class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        output = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                if intervals[i][1] <= output[-1][1]:
                    continue
                else:
                    output[-1] = [output[-1][0],intervals[i][1]]
            else:
                output.append(intervals[i])
        return output