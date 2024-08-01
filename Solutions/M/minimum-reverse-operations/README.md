# Minimum reverse operations

[Problem link](https://leetcode.com/problems/minimum-reverse-operations/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-reverse-operations/

class Solution {
 public:
  vector<int> minReverseOperations(int n, int p, vector<int>& banned, int k) {
    auto range = [&](int u) {
      int l1 = max(u - k + 1, 0), r1 = l1 + k - 1, r2 = min(u + k - 1, n - 1),
          l2 = r2 - k + 1;
      int l = l1 + r1 - u, r = l2 + r2 - u;
      return make_pair(l, r);
    };
    unordered_set<int> bad;
    for (int x : banned) bad.insert(x);

    set<int> todo[2];
    for (int i = 0; i < n; ++i)
      if (!bad.count(i)) todo[i & 1].insert(i);
    todo[p & 1].erase(p);

    vector<int> ret(n, -1);
    ret[p] = 0;
    queue<int> bfsq;
    bfsq.push(p);

    while (!bfsq.empty()) {
      int u = bfsq.front();
      bfsq.pop();

      auto [l, r] = range(u);
      auto par = (k ^ u ^ 1) & 1;
      for (auto it = todo[par].lower_bound(l);
           it != todo[par].end() and *it <= r; todo[par].erase(it++)) {
        int v = *it;
        ret[v] = ret[u] + 1;
        bfsq.push(v);
      }
    }
    return ret;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search) > [C++ set](/Collections/binary-search.md#c---set)
* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Parity](/Collections/mathematics.md#parity)
