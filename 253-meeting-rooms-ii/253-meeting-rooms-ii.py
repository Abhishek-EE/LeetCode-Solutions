class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms_available = [intervals[0][1]]
        heapify(rooms_available)
        num_of_rooms = 1
        for i in range(1,len(intervals)):
            earliest_available_room = rooms_available[0]
            if intervals[i][0] >= earliest_available_room:
                heapreplace(rooms_available,intervals[i][1])
            else:
                heappush(rooms_available,intervals[i][1])
                num_of_rooms += 1
        
        return num_of_rooms
                
        