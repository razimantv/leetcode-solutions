# Unique paths

[Problem link](https://leetcode.com/problems/unique-paths)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/unique-paths

class Solution {
 public:
  int uniquePaths(int m, int n) {
    int N = m + n - 2, R = min(m, n) - 1;
    double ret = 1;
    for (int i = 0; i < R; i++) ret *= N - i;
    for (int i = 1; i <= R; i++) ret /= i;
    return (int)ret;
  }
};
```