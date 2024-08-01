# Lexicographically smallest equivalent string

[Problem link](https://leetcode.com/problems/lexicographically-smallest-equivalent-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/lexicographically-smallest-equivalent-string

class Solution {
 public:
  string smallestEquivalentString(string s1, string s2, string baseStr) {
    vector<char> par(26);
    iota(par.begin(), par.end(), 0);
    function<int(int)> parent = [&](int u) {
      return par[u] == u ? u : par[u] = parent(par[u]);
    };

    for (int i = 0; s1[i]; ++i) {
      char u = parent(s1[i] - 'a'), v = parent(s2[i] - 'a');
      par[max(u, v)] = min(u, v);
    }

    for (char& c : baseStr) c = parent(c - 'a') + 'a';
    return baseStr;
  }
};
```
## Tags

* [Disjoint set union](/Collections/disjoint-set-union.md#disjoint-set-union)
