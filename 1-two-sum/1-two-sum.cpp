class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> conjugate_map; //Stores indexes

        for(int i=0; i<nums.size(); i++){
            if(conjugate_map.count(target - nums[i])){
                return {conjugate_map[target - nums[i]],i};
            }
            conjugate_map[nums[i]] = i;
        }
        
        return {};
        
    }
};