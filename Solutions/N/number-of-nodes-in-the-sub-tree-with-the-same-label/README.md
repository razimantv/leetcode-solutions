# Number of nodes in the sub tree with the same label

[Problem link](https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/

class Solution {
 public:
  vector<int> countSubTrees(int n, vector<vector<int>>& edges, string labels) {
    vector<vector<int>> adj(n);
    for (const auto& e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    vector<int> ret(n);
    using mymap = unordered_map<char, int>;
    std::function<mymap(int, int)> dfs = [&](int u, int par) {
      mymap cur{{labels[u], 1}};
      for (int v : adj[u]) {
        if (v == par) continue;
        for (auto [k, v] : dfs(v, u)) cur[k] += v;
      }
      ret[u] = cur[labels[u]];
      return cur;
    };

    dfs(0, -1);
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Hashmap](/Collections/hashmap.md#hashmap)
