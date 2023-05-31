# Sort items by groups respecting dependencies

[Problem link](https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies

class Solution {
 public:
  vector<int> toposort(vector<int>& vertices, vector<int>& indegree,
                       vector<vector<int>>& adj) {
    int X = vertices.size();
    queue<int> todo;
    for (int u : vertices)
      if (!indegree[u]) todo.push(u);

    vector<int> ret;
    while (!todo.empty()) {
      --X;
      int u = todo.front();
      ret.push_back(u);
      todo.pop();
      for (int v : adj[u])
        if (--indegree[v] == 0) todo.push(v);
    }
    if (X) return {};
    reverse(ret.begin(), ret.end());
    return ret;
  }

  vector<int> sortItems(int n, int m, vector<int>& group,
                        vector<vector<int>>& beforeItems) {
    for (int u = 0; u < n; ++u)
      if (group[u] == -1) group[u] = m++;
    vector<int> group_indegree(m), vertex_indegree(n);
    vector<vector<int>> group_before(m), group_elements(m);
    for (int u = 0; u < n; ++u) {
      int gu = group[u];
      group_elements[gu].push_back(u);
      for (int i = 0; i < beforeItems[u].size(); ++i) {
        int v = beforeItems[u][i], gv = group[v];
        if (gu == gv) {
          ++vertex_indegree[v];
        } else {
          group_before[gu].push_back(gv);
          ++group_indegree[gv];
          swap(beforeItems[u][i--], beforeItems[u].back());
          beforeItems[u].pop_back();
        }
      }
    }

    vector<int> groups(m);
    iota(groups.begin(), groups.end(), 0);
    auto group_order = toposort(groups, group_indegree, group_before);
    if (group_order.empty()) return {};
    vector<int> ret;
    for (int g : group_order) {
      if (group_elements[g].empty()) continue;
      auto vertex_order =
          toposort(group_elements[g], vertex_indegree, beforeItems);
      if (vertex_order.empty()) return {};
      ret.insert(ret.end(), vertex_order.begin(), vertex_order.end());
    }
    return ret;
  }
};
```