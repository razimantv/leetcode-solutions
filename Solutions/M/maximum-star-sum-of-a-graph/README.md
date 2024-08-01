# Maximum star sum of a graph

[Problem link](https://leetcode.com/problems/maximum-star-sum-of-a-graph/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-star-sum-of-a-graph/

class Solution {
 public:
  int maxStarSum(vector<int>& vals, vector<vector<int>>& edges, int k) {
    int n = vals.size();
    vector<vector<int>> adj(n);
    for (auto& e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    int best = INT_MIN;
    for (int i = 0; i < n; ++i) {
      sort(adj[i].begin(), adj[i].end(),
           [&](int u, int v) { return vals[u] > vals[v]; });
      int cur = vals[i], j = 0;
      for (int v : adj[i])
        if (++j > k or vals[v] <= 0)
          break;
        else
          cur += vals[v];
      best = max(best, cur);
    }
    return best;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
* [Sorting](/Collections/sorting.md#sorting)
