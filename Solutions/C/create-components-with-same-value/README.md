# Create components with same value

[Problem link](https://leetcode.com/problems/create-components-with-same-value/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/create-components-with-same-value/

class Solution {
 public:
  int dfs(int u, int par, int poss, const vector<int>& nums,
          const vector<vector<int>>& adj) {
    int cur = nums[u];
    for (int v : adj[u]) {
      if (v != par) {
        int child = dfs(v, u, poss, nums, adj);
        if (child == -1 or (cur += child) > poss) return -1;
      }
    }
    return cur % poss;
  }
  int componentValue(vector<int>& nums, vector<vector<int>>& edges) {
    int tot = accumulate(nums.begin(), nums.end(), 0);
    int m = *max_element(nums.begin(), nums.end());
    vector<int> poss;
    for (int x = 1; x * x <= tot; ++x) {
      if (tot % x) continue;
      poss.push_back(x);
      if (x > 1 and x * x < tot) poss.push_back(tot / x);
    }
    sort(poss.begin(), poss.end());
    int V = poss.size();
    vector<bool> good(V, true);

    int N = nums.size();
    vector<vector<int>> adj(N);
    for (auto& e : edges) {
      adj[e[0]].push_back(e[1]);
      adj[e[1]].push_back(e[0]);
    }

    for (int x : poss) {
      if (x < m) continue;
      if (dfs(0, -1, x, nums, adj) == 0) return tot / x - 1;
    }
    return 0;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Factor listing in sqrt(N)](/Collections/mathematics.md#factor-listing-in-sqrt-n-)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
