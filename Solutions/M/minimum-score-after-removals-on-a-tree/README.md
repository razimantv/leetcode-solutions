# Minimum score after removals on a tree

[Problem link](https://leetcode.com/problems/minimum-score-after-removals-on-a-tree)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree

class Solution {
 public:
  int X, best;
  vector<vector<int>> adj;
  vector<int> nums;

  vector<int> dfs(int u, int par) {
    vector<vector<int>> children;
    int subtreexor = nums[u];
    int C = 0, maxc = 0;
    for (int v : adj[u]) {
      if (v == par) continue;
      children.push_back(dfs(v, u));
      int childtreexor = children[C].back();
      subtreexor ^= childtreexor;
      for (int i = 0, n = children[C].size(); i < n - 1; ++i) {
        vector<int> cur{children[C][i], childtreexor ^ children[C][i],
                        X ^ childtreexor};
        sort(cur.begin(), cur.end());
        best = min(best, cur[2] - cur[0]);
      }

      for (int i = 0; i < C; ++i)
        for (int x : children[i])
          for (int y : children[C]) {
            vector<int> cur{x, y, X ^ x ^ y};
            sort(cur.begin(), cur.end());
            best = min(best, cur[2] - cur[0]);
          }
      if (children[C].size() > children[maxc].size()) maxc = C;
      ++C;
    }
    if (!C) return {subtreexor};

    for (int i = 0; i < C; ++i) {
      if (i == maxc) continue;
      children[maxc].insert(children[maxc].end(), children[i].begin(),
                            children[i].end());
    }
    children[maxc].push_back(subtreexor);
    return children[maxc];
  }
  int minimumScore(vector<int>& nums, vector<vector<int>>& edges) {
    int N = nums.size();
    this->nums = nums;
    X = accumulate(nums.begin(), nums.end(), 0,
                   [](int a, int b) { return a ^ b; });
    adj.resize(N);
    for (auto& e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    best = INT_MAX;
    dfs(0, -1);
    return best;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
