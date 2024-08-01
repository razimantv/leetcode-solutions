# Jump game iii

[Problem link](https://leetcode.com/problems/jump-game-iii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/jump-game-iii

class Solution {
 public:
  bool canReach(vector<int>& arr, int u) {
    if (!arr[u])
      return true;
    else if (arr[u] < 0)
      return false;

    int j = arr[u];
    arr[u] = -j;

    if (u >= j and canReach(arr, u - j)) return true;
    if (u + j < arr.size() and canReach(arr, u + j)) return true;
    return false;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
