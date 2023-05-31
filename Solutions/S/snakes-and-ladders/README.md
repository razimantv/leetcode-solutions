# Snakes and ladders

[Problem link](https://leetcode.com/problems/snakes-and-ladders)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/snakes-and-ladders

class Solution {
 public:
  vector<int> board_conv;
  int snakesAndLadders(vector<vector<int>>& board) {
    int m = board.size(), n = board[0].size();
    board_conv = {0};
    for (int i = m - 1, rev = 0; i >= 0; --i, rev = 1 - rev) {
      if (rev) reverse(board[i].begin(), board[i].end());
      copy(board[i].begin(), board[i].end(), back_inserter(board_conv));
    }

    vector<int> dist(m * n + 1, -1);
    queue<int> bfsq;
    bfsq.push(1);
    dist[1] = 0;
    while (!bfsq.empty()) {
      int u = bfsq.front();
      bfsq.pop();
      for (int i = 1; i <= 6; ++i) {
        int v = u + i;
        if (board_conv[v] != -1) v = board_conv[v];
        if (dist[v] == -1) {
          dist[v] = dist[u] + 1;
          if (v == m * n) return dist[v];
          bfsq.push(v);
        }
      }
    }
    return -1;
  }
};
```