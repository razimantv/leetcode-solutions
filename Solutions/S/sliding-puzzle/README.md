# Sliding puzzle

[Problem link](https://leetcode.com/problems/sliding-puzzle)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sliding-puzzle

class Solution {
 public:
  int slidingPuzzle(vector<vector<int>>& b) {
    typedef vector<vector<int>> board;
    map<board, int> seen;
    board start{{1, 2, 3}, {4, 5, 0}};
    seen[start] = 0;
    queue<board> bfs;
    bfs.push(start);

    while (!bfs.empty()) {
      auto cur = bfs.front();
      int d = seen[cur];
      if (cur == b) return d;
      bfs.pop();

      int ii = 0, jj = 0;
      for (ii = 0; ii < 2; ++ii)
        for (jj = 0; jj < 3; ++jj)
          if (cur[ii][jj] == 0) goto BPP;
    BPP:;

      if (jj) {
        swap(cur[ii][jj], cur[ii][jj - 1]);
        if (!seen.count(cur)) {
          seen[cur] = d + 1;
          bfs.push(cur);
        }
        swap(cur[ii][jj], cur[ii][jj - 1]);
      }
      if (jj < 2) {
        swap(cur[ii][jj], cur[ii][jj + 1]);
        if (!seen.count(cur)) {
          seen[cur] = d + 1;
          bfs.push(cur);
        }
        swap(cur[ii][jj], cur[ii][jj + 1]);
      }
      swap(cur[ii][jj], cur[1 - ii][jj]);
      if (!seen.count(cur)) {
        seen[cur] = d + 1;
        bfs.push(cur);
      }
      swap(cur[ii][jj], cur[1 - ii][jj]);
    }
    return -1;
  }
};
```