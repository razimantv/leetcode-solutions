# Accounts merge

[Problem link](https://leetcode.com/problems/accounts-merge)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/accounts-merge

class Solution {
 public:
  vector<int> parent;
  int par(int u) { return parent[u] == u ? u : (parent[u] = par(parent[u])); }

  void merge(int u, int v) {
    u = par(u), v = par(v);
    if (u != v) parent[u] = v;
  }

  vector<vector<string>> accountsMerge(vector<vector<string>>& accounts) {
    int N = accounts.size();
    parent.resize(N);
    iota(parent.begin(), parent.end(), 0);

    unordered_map<string, int> m;
    for (int i = 0; i < N; ++i) {
      int S = accounts[i].size();
      for (int j = 1; j < S; ++j) {
        auto s = accounts[i][j];
        if (m.count(s))
          merge(i, m[s]);
        else
          m[s] = i;
      }
    }

    vector<unordered_set<string>> v(N);
    for (int i = 0; i < N; ++i) {
      int S = accounts[i].size();
      for (int j = 1; j < S; ++j) v[par(i)].insert(accounts[i][j]);
    }

    vector<vector<string>> ret;
    for (int i = 0; i < N; ++i) {
      if (v[i].empty()) continue;
      ret.push_back({accounts[i][0]});
      for (const string& s : v[i]) ret.back().push_back(s);
      sort(ret.back().begin() + 1, ret.back().end());
    }

    return ret;
  }
};
```
## Tags

* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
