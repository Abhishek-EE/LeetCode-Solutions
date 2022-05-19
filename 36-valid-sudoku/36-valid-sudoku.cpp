class Solution {
public:
    bool isElemValid(char elem,std::unordered_set<char>& set_of_values){
        if(elem == '.')
            return true;
        if(static_cast<int>(elem-'0') < 1 || static_cast<int>(elem-'0') > 9){
            // std::cout<<static_cast<int>(elem-'0')<<" "<<elem<<"\n";
            return false;
        }
        if(set_of_values.count(elem))
            return false;
        return true;
                
        }

    bool isValidSudoku(vector<vector<char>>& board) {
        std::unordered_set<char> row_set, col_set, mini_sudoku_set;
        char row_elem, col_elem, mini_sudoku_elem;
        //This is testing for whether the row and columns are valid
        //I can also test for whether the mini sudoku is valid
        for(int i=0; i<board.size(); i++){
            row_set.clear();
            col_set.clear();
            for(int j=0; j<board.size(); j++){
                row_elem = board[i][j];
                col_elem = board[j][i];
                if(!isElemValid(row_elem, row_set))
                    return false;
                if(!isElemValid(col_elem, col_set))
                    return false;
                row_set.insert(row_elem);
                col_set.insert(col_elem);
            }
        }
        //Iterate through mini sudoku
        for(int hor =0; hor<3; hor++)
            for(int ver=0; ver<3; ver++){
                mini_sudoku_set.clear();
                for(int i=0; i<3; i++)
                    for(int j=0; j<3; j++){
                        mini_sudoku_elem = board[hor*3+i][ver*3+ j];
                        if(!isElemValid(mini_sudoku_elem,mini_sudoku_set))
                            return false;
                        mini_sudoku_set.insert(mini_sudoku_elem);
                    }
            }

    return true;    
    }
};