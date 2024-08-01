# Evaluate division

[Problem link](https://leetcode.com/problems/evaluate-division)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/evaluate-division

class Solution {
  unordered_map<string, vector<pair<string, int>>> adjlist;
  unordered_map<string, int> comp;
  unordered_map<string, double> val;

  void dfs(const string& u, const vector<vector<string>>& equations,
           const vector<double>& values) {
    for (const auto& [v, eq] : adjlist[u]) {
      if (comp.count(v)) continue;
      if (v == equations[eq][0])
        val[v] = val[u] * values[eq];
      else
        val[v] = val[u] / values[eq];
      comp[v] = comp[u];
      dfs(v, equations, values);
    }
  }

 public:
  vector<double> calcEquation(vector<vector<string>>& equations,
                              vector<double>& values,
                              vector<vector<string>>& queries) {
    int N = equations.size();
    for (int i = 0; i < N; ++i) {
      adjlist[equations[i][0]].push_back({equations[i][1], i});
      adjlist[equations[i][1]].push_back({equations[i][0], i});
    }

    int nextcomp{0};
    vector<double> ret;
    for (const auto& [u, row] : adjlist) {
      if (comp.count(u)) continue;
      val[u] = 1;
      comp[u] = ++nextcomp;
      dfs(u, equations, values);
    }

    for (auto q : queries) {
      ret.push_back(
          (comp.count(q[0]) and comp.count(q[1]) and comp[q[0]] == comp[q[1]])
              ? (val[q[0]] / val[q[1]])
              : -1);
    }
    return ret;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Component decomposition](/Collections/graph-theory.md#component-decomposition)
