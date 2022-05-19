class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        Brute Force approach ->
        Find the area of water stroed between all the possible combination of arrays
        return the combination with maximum area
        Solution is big O(n)
        so basically this is a maximization problem where the product of two variable needs to be maxizied
        product = min(height[i],height[i+L])*L
        two different things to be maximized are height[i]
        and L -> distance between two points
        ok so the approach can be that you chose two pointers one at the beginning and one at the end
        find the area and move the smaller of the two.
        Until you reach the mid value
        '''
        end_pointer = len(height) - 1
        start_pointer = 0
        max_volume = 0
        while(end_pointer-start_pointer>0):
            volume = min(height[start_pointer],height[end_pointer])*(end_pointer-start_pointer)
            max_volume = max(max_volume,volume)
            if(height[start_pointer] < height[end_pointer]):
                start_pointer += 1
            else:
                end_pointer -= 1
                
        return max_volume
        