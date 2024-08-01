# Count pairs of nodes

[Problem link](https://leetcode.com/problems/count-pairs-of-nodes)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-pairs-of-nodes

class Solution {
 public:
  vector<int> countPairs(int n, vector<vector<int>>& edges,
                         vector<int>& queries) {
    vector<int> degree(n);
    map<pair<int, int>, int> cnt;
    for (auto& e : edges) {
      int &u = e[0], &v = e[1];
      if (u > v) swap(u, v);
      degree[u - 1]++;
      degree[v - 1]++;
      cnt[{u - 1, v - 1}]++;
    }

    vector<int> ans;
    auto dcopy = degree;
    sort(dcopy.begin(), dcopy.end());
    for (int q : queries) {
      int l = 0, r = n - 1, ret = 0;
      while (l < n and dcopy[l] + dcopy[r] <= q) ++l;
      for (; l < n; ++l) {
        while (r >= 0 and dcopy[l] + dcopy[r] > q) --r;
        ret += n - 1 - max(r, l);
      }

      for (auto [uv, c] : cnt) {
        auto [u, v] = uv;
        if (degree[u] + degree[v] > q and degree[u] + degree[v] - c <= q) --ret;
      }
      ans.push_back(ret);
    }
    return ans;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
