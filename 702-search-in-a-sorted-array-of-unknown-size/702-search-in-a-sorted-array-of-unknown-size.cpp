/**
 * // This is the ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * class ArrayReader {
 *   public:
 *     int get(int index);
 * };
 */

class Solution {
public:
    int search(const ArrayReader& reader, int target) {
        int start = 0;
        int end = 1;
        while(reader.get(end)<target){
            start = end;
            end = 2*end;
        }
        int mid = start + (end-start)/2;
        while(end-start>=0){
            if(reader.get(mid) == target)
                return mid;
            else if(reader.get(mid) < target)
                start = mid + 1;
            else
                end = mid - 1;
            mid = start + (end-mid)/2;
            
        }
        return -1;
        
    }
};