# Find winner on a tic tac toe game

[Problem link](https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game

class Solution {
 public:
  string tictactoe(vector<vector<int>>& moves) {
    vector<tuple<int, int, int, int>> ijd{
        {0, 0, 0, 1}, {1, 0, 0, 1}, {2, 0, 0, 1}, {0, 0, 1, 0},
        {0, 1, 1, 0}, {0, 2, 1, 0}, {0, 0, 1, 1}, {0, 2, 1, -1}};

    char board[3][3];
    memset(board, 0, sizeof(board));
    for (int i = 0, m = moves.size(); i < m; ++i)
      board[moves[i][0]][moves[i][1]] = 'A' + (i & 1);
    for (auto [i, j, di, dj] : ijd)
      if (board[i][j] and board[i][j] == board[i + di][j + dj] and
          board[i][j] == board[i + 2 * di][j + 2 * dj])
        return string(1, board[i][j]);
    return moves.size() == 9 ? "Draw" : "Pending";
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
