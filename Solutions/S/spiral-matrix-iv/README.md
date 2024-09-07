# Spiral matrix iv

[Problem link](https://leetcode.com/problems/spiral-matrix-iv)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/spiral-matrix-iv

class Solution {
 public:
  vector<vector<int>> spiralMatrix(int m, int n, ListNode* head) {
    vector<vector<int>> mat(m, vector<int>(n, -1));

    vector<pair<int, int>> dirn{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int lowx = 0, lowy = 0, highx = m - 1, highy = n - 1;
    for (int done = 0, dir = 0, x = 0, y = 0; head and done < m * n; ++done) {
      mat[x][y] = head->val;
      head = head->next;

      auto [dx, dy] = dirn[dir];
      int newx = x + dx, newy = y + dy;
      if (newx < lowx or newx > highx or newy < lowy or newy > highy) {
        if (dir == 0)
          ++lowx;
        else if (dir == 1)
          --highy;
        else if (dir == 2)
          --highx;
        else
          ++lowy;

        dir = (dir + 1) & 3;
        auto [dx, dy] = dirn[dir];
        newx = x + dx, newy = y + dy;
      }
      // cout << x << " " << y << " " << mat[x][y] << " " << dir << " " << newx
      // << " " << newy << "\n";
      x = newx, y = newy;
    }
    return mat;
  }
};
```