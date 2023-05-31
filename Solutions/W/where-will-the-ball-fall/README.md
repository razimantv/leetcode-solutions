# Where will the ball fall

[Problem link](https://leetcode.com/problems/where-will-the-ball-fall)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/where-will-the-ball-fall

class Solution {
public:
  vector<int> findBall(vector<vector<int>> &grid) {
    int m = grid.size(), n = grid[0].size();
    vector<int> ret(n, -1);

    for (int c = 0; c < n; ++c) {
      int j = c;
      for (int i = 0; i < m; ++i) {
        int jj = j + grid[i][j];
        if (jj == -1 or jj == n or grid[i][jj] != grid[i][j])
          goto BPP;
        j = jj;
      }
      ret[c] = j;
    BPP:;
    }
    return ret;
  }
};
```
## Tags

* [Matrix](/README.md#Matrix) > [Path](/README.md#Matrix-Path)
* [Graph theory](/README.md#Graph_theory) > [Single outdegree graphs](/README.md#Graph_theory-Single_outdegree_graphs)
