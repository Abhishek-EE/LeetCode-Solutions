class Solution {
public:
    bool isOpen(char& c){
        if(c=='(' || c=='{' || c=='[')
            return true;
        return false;
    }
    
    bool isValid(string s) {
        stack<char> bracket_stack;
        unordered_map<char,char> char_map{ {'(',')'}, {'{','}'}, {'[',']'} };
        if(s.size() == 0)
            return true;
        for(auto i: s){
            if(char_map.count(i)){
                bracket_stack.push(i);
            }
            else{
                if(bracket_stack.empty() || i != char_map[bracket_stack.top()]){
                    return false;
                }
                bracket_stack.pop();
            }
        }
        if(bracket_stack.empty())
            return true;
        return false;
    }
};