# Detonate the maximum bombs

[Problem link](https://leetcode.com/problems/detonate-the-maximum-bombs/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/detonate-the-maximum-bombs/

class Solution {
 public:
  int maximumDetonation(vector<vector<int>>& bombs) {
    int n = bombs.size();
    auto reachable = [&](int u, int v) {
      long long dx = bombs[v][0] - bombs[u][0], dy = bombs[v][1] - bombs[u][1],
                r = bombs[u][2];
      return dx * dx + dy * dy <= r * r;
    };
    auto count = [&](int start) {
      vector<int> seen(n);
      queue<int> bfsq;
      bfsq.push(start);
      seen[start] = 1;
      int ret{};
      while (!bfsq.empty()) {
        int u = bfsq.front();
        bfsq.pop();
        ++ret;

        for (int v = 0; v < n; ++v) {
          if (!seen[v] and reachable(u, v)) {
            seen[v] = 1;
            bfsq.push(v);
          }
        }
      }
      return ret;
    };

    int best{};
    for (int i = 0; i < n; ++i) best = max(best, count(i));
    return best;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
