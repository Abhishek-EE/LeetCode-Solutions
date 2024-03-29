class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        """
        A person can't attend meeting if any two intervals have any sort of intersection
        easiest approach is to sort all the meetings by start time and if end time of any meeting is greater than start time of any other meeting then it can't be attended
        """
        intervals.sort()
        for i in range(1,len(intervals)):
            if intervals[i-1][1] > intervals[i][0]:
                return False
        return True
            