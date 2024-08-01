# Number of ways to paint n 3 grid

[Problem link](https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-ways-to-paint-n-3-grid

class Solution {
 public:
  vector<int> masktovec(int mask) {
    vector<int> ret;
    for (int i = 0; i < 3; ++i, mask /= 3) ret.push_back(mask % 3);
    return ret;
  }

  bool valid(const vector<int>& state) {
    return state[0] != state[1] and state[1] != state[2];
  }

  bool valid(const vector<int>& state1, const vector<int>& state2) {
    for (int i = 0; i < 3; ++i)
      if (state1[i] == state2[i]) return false;
    return true;
  }

  int numOfWays(int n) {
    vector<vector<int>> validstates;
    for (int i = 0; i < 27; ++i) {
      auto state = masktovec(i);
      if (valid(state)) validstates.push_back(state);
    }

    int V = validstates.size();
    vector<int> cnt(V, 1);
    vector<vector<int>> adj(V);
    for (int i = 0; i < V; ++i)
      for (int j = 0; j < i; ++j)
        if (valid(validstates[i], validstates[j]))
          adj[i].push_back(j), adj[j].push_back(i);

    const int MOD = 1'000'000'007;
    for (int i = 1; i < n; ++i) {
      vector<int> next(V);
      for (int i = 0; i < V; ++i) {
        for (int j : adj[i]) {
          next[j] += cnt[i];
          if (next[j] >= MOD) next[j] -= MOD;
        }
      }
      cnt = next;
    }

    return accumulate(cnt.begin(), cnt.end(), 0ll) % MOD;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Graph-like state transitions](/Collections/dynamic-programming.md#graph-like-state-transitions)
