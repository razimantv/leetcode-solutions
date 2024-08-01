# Out of boundary paths

[Problem link](https://leetcode.com/problems/out-of-boundary-paths)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/out-of-boundary-paths

class Solution {
 public:
  map<tuple<int, int, int>, int> cache;
  const int MOD = 1'000'000'007;
  const int neigh[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

  int work(int i, int j, int M, int N, int steps) {
    if (steps == 1) return (i == 0) + (i == M - 1) + (j == 0) + (j == N - 1);
    if (cache.count({i, j, steps})) return cache[{i, j, steps}];

    int ret = 0;
    for (auto [di, dj] : neigh) {
      int ii = i + di, jj = j + dj;
      if (ii >= 0 and ii < M and jj >= 0 and jj < N) {
        ret += work(ii, jj, M, N, steps - 1);
        if (ret >= MOD) ret -= MOD;
      }
    }
    return cache[{i, j, steps}] = ret;
  }
  int findPaths(int m, int n, int maxMove, int r, int c) {
    int ret = 0;
    for (int i = 1; i <= maxMove; ++i) {
      ret += work(r, c, m, n, i);
      if (ret >= MOD) ret -= MOD;
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
