# Sum of distances in tree

[Problem link](https://leetcode.com/problems/sum-of-distances-in-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sum-of-distances-in-tree

class Solution {
 public:
  vector<vector<int>> adj;
  vector<int> seen, sz, ret;
  int N;
  void work1(int u) {
    seen[u] = sz[u] = 1;
    for (int v : adj[u]) {
      if (seen[v]) continue;
      work1(v);
      sz[u] += sz[v];
      ret[u] += ret[v] + sz[v];
    }
  }

  void work2(int u) {
    seen[u] = 2;
    for (int v : adj[u]) {
      if (seen[v] == 2) continue;
      ret[v] += ret[u] - ret[v] - sz[v] + N - sz[v];
      work2(v);
    }
  }
  vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
    N = n;
    adj.resize(n);
    for (auto& e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    seen = sz = ret = vector<int>(n);
    work1(0);
    work2(0);
    return ret;
  }
};
```