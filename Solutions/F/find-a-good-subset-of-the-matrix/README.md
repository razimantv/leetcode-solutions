# Find a good subset of the matrix

[Problem link](https://leetcode.com/problems/find-a-good-subset-of-the-matrix/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-a-good-subset-of-the-matrix/

class Solution {
 public:
  vector<int> goodSubsetofBinaryMatrix(vector<vector<int>>& grid) {
    auto getmask = [](const auto& v) {
      int ret{};
      for (int x : v) ret = (ret << 1) | x;
      return ret;
    };

    unordered_map<int, int> seen;
    for (int i = 0, n = grid.size(); i < n; ++i) {
      int m = getmask(grid[i]);
      if (!m) return {i};
      if (seen.count(m)) continue;
      for (auto [k, v] : seen)
        if (!(k & m)) return {v, i};
      seen[m] = i;
    }
    return {};
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Reduce problem dimension with proofs](/Collections/mathematics.md#reduce-problem-dimension-with-proofs)
