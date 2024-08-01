# Jump game iv

[Problem link](https://leetcode.com/problems/jump-game-iv)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/jump-game-iv

class Solution {
 public:
  int minJumps(vector<int>& ar) {
    unordered_map<int, vector<int>> m;
    int n = ar.size();
    for (int i = 0; i < n; ++i) m[ar[i]].push_back(i);

    vector<int> d(n, -1);
    queue<int> q;

    q.push(0);
    d[0] = 0;
    while (1) {
      int u = q.front();
      if (u == n - 1) return d[u];
      q.pop();

      if (u + 1 < n and d[u + 1] == -1) {
        d[u + 1] = d[u] + 1;
        q.push(u + 1);
      }
      if (u > 0 and d[u - 1] == -1) {
        d[u - 1] = d[u] + 1;
        q.push(u - 1);
      }
      for (int v : m[ar[u]]) {
        if (d[v] == -1) {
          d[v] = d[u] + 1;
          q.push(v);
        }
      }
      m[ar[u]].clear();
    }
    return -1;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Group items](/Collections/hashmap.md#group-items)
