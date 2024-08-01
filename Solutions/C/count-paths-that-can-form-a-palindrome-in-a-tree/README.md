# Count paths that can form a palindrome in a tree

[Problem link](https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

class Solution {
 public:
  unordered_map<int, int> cnt;
  void dfs(vector<vector<pair<int, char>>>& adj, int u, int pref) {
    ++cnt[pref];
    for (auto [v, c] : adj[u]) dfs(adj, v, pref ^ (1 << (c - 'a')));
  }
  long long countPalindromePaths(vector<int>& parent, string s) {
    int n = s.size();
    vector<vector<pair<int, char>>> adj(n);
    for (int i = 1; s[i]; ++i) adj[parent[i]].push_back({i, s[i]});
    dfs(adj, 0, 0);
    long long ret{};
    for (auto [k, v] : cnt) {
      ret += (v * (v - 1ll)) / 2;
      for (int i = 0; i < 26; ++i) {
        if (k & (1 << i)) continue;
        int kk = k ^ (1 << i);
        if (cnt.count(kk)) ret += v * 1ll * cnt[kk];
      }
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation) > [Self-inverse property of xor](/Collections/bitwise-operation.md#self-inverse-property-of-xor)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Palindrome](/Collections/palindrome.md#palindrome)
