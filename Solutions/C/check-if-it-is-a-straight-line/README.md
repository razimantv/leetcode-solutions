# Check if it is a straight line

[Problem link](https://leetcode.com/problems/check-if-it-is-a-straight-line)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/check-if-it-is-a-straight-line

class Solution {
 public:
  bool checkStraightLine(vector<vector<int>>& coordinates) {
    int N = coordinates.size();
    if (N < 3) return true;

    int dx = coordinates[1][0] - coordinates[0][0],
        dy = coordinates[1][1] - coordinates[0][1];
    for (int i = 2; i < N; i++) {
      int dxp = coordinates[i][0] - coordinates[0][0],
          dyp = coordinates[i][1] - coordinates[0][1];
      if (dxp * dy != dyp * dx) return false;
    }
    return true;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Geometry](/Collections/mathematics.md#geometry)
