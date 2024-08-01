# Minimum operations to convert number

[Problem link](https://leetcode.com/problems/minimum-operations-to-convert-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-operations-to-convert-number

class Solution {
 public:
  int minimumOperations(vector<int>& nums, int start, int goal) {
    queue<int> bfsq;
    int seen[1001] = {0};
    bfsq.push(start);
    seen[start] = 1;
    int done = 0;
    while (!bfsq.empty() and ++done < 2000) {
      int u = bfsq.front();
      bfsq.pop();
      for (int x : nums) {
        vector<int> next{u + x, u - x, u ^ x};
        for (int v : next) {
          if (v == goal)
            return seen[u];
          else if (v >= 0 and v <= 1000 and !seen[v]) {
            seen[v] = seen[u] + 1;
            bfsq.push(v);
          }
        }
      }
    }
    return -1;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Breadth first search](/Collections/graph-theory.md#breadth-first-search)
