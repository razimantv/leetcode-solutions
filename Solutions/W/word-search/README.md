# Word search

[Problem link](https://leetcode.com/problems/word-search)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/word-search

class Solution {
 public:
  bool exist(vector<vector<char>>& board, string& word, int pos = 0, int i = -1,
             int j = -1) {
    if (i >= 0 and pos == word.size() - 1) return true;
    if (i == -1) {
      for (int i = 0; i < board.size(); ++i)
        for (int j = 0; j < board[i].size(); ++j)
          if (board[i][j] == word[0] and exist(board, word, 0, i, j))
            return true;
      return false;
    }
    board[i][j] = '#';
    vector<vector<int>> dir = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    for (auto d : dir) {
      int ii = i + d[0], jj = j + d[1];
      if (ii >= 0 and ii < board.size() and jj >= 0 and jj < board[0].size() and
          board[ii][jj] == word[pos + 1] and
          exist(board, word, pos + 1, ii, jj))
        return true;
    }
    board[i][j] = word[pos];
    return false;
  }
};
```