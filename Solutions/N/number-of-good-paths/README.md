# Number of good paths

[Problem link](https://leetcode.com/problems/number-of-good-paths/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-good-paths/

class Solution {
 public:
  vector<int> par;
  int parent(int u) { return (par[u] == u) ? u : (par[u] = parent(par[u])); }
  int numberOfGoodPaths(vector<int>& vals, vector<vector<int>>& edges) {
    map<int, pair<vector<int>, vector<pair<int, int>>>> sorted;
    int n = vals.size();
    par.resize(n);
    iota(par.begin(), par.end(), 0);

    for (int i = 0; i < n; ++i) sorted[vals[i]].first.push_back(i);
    for (auto& e : edges) {
      int u = e[0], v = e[1];
      sorted[max(vals[u], vals[v])].second.push_back({u, v});
    }

    int answer = 0;
    for (auto& [val, vevec] : sorted) {
      auto& [vvec, evec] = vevec;
      for (auto [u, v] : evec) par[parent(u)] = parent(v);
      unordered_map<int, int> cnt;
      for (int u : vvec) answer += ++cnt[parent(u)];
    }
    return answer;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Group items](/Collections/hashmap.md#group-items)
* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Sorting](/Collections/sorting.md#sorting) > [Queries and updates together](/Collections/sorting.md#queries-and-updates-together)
