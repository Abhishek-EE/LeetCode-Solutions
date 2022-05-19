class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for (int i=0; i<matrix.size(); i++)
            for(int j=i; j<matrix.size(); j++){
                swap(matrix[i][j], matrix[j][i]);
            }
        for(auto& i: matrix)
            reverse(i.begin(), i.end());
    }
};