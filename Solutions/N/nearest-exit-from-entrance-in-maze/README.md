# Nearest exit from entrance in maze

[Problem link](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution {
 public:
  int nearestExit(vector<vector<char>>& maze, vector<int>& entrance) {
    int m = maze.size(), n = maze[0].size();
    queue<tuple<int, int, int>> bfsq;
    int sx = entrance[0], sy = entrance[1];
    maze[sx][sy] = '+';
    bfsq.push({sx, sy, 0});
    const vector<pair<int, int>> neigh{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    while (!bfsq.empty()) {
      auto [x, y, d] = bfsq.front();
      bfsq.pop();
      for (auto [dx, dy] : neigh) {
        int xx = x + dx, yy = y + dy;
        if (xx < 0 or yy < 0 or xx >= m or yy >= n or maze[xx][yy] != '.')
          continue;
        if (xx == 0 or yy == 0 or xx == m - 1 or yy == n - 1) return d + 1;
        maze[xx][yy] = '+';
        bfsq.push({xx, yy, d + 1});
      }
    }
    return -1;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
