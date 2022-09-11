class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms_available = []
        room_not_available = True
        for i in range(len(intervals)):
            for j in range(len(rooms_available)):
                if intervals[i][0] >= rooms_available[j]:
                    rooms_available[j] = intervals[i][1]
                    room_not_available = False
                    break
            if room_not_available:
                rooms_available.append(intervals[i][1])
            room_not_available = True
        return len(rooms_available)
                
        