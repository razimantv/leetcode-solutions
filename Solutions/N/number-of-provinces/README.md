# Number of provinces

[Problem link](https://leetcode.com/problems/number-of-provinces/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-provinces/

#include <vector>

// ChatGPT solution
class Solution {
 public:
  void dfs(int city, std::vector<std::vector<int>>& isConnected,
           std::vector<bool>& visited) {
    visited[city] = true;
    for (int i = 0; i < isConnected.size(); i++) {
      if (isConnected[city][i] == 1 && !visited[i]) {
        dfs(i, isConnected, visited);
      }
    }
  }

  int findCircleNum(std::vector<std::vector<int>>& isConnected) {
    int n = isConnected.size();
    std::vector<bool> visited(n, false);
    int provinceCount = 0;

    for (int i = 0; i < n; i++) {
      if (!visited[i]) {
        dfs(i, isConnected, visited);
        provinceCount++;
      }
    }

    return provinceCount;
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search) > [Component decomposition](/Collections/graph-theory.md#component-decomposition)
* [ChatGPT](/Collections/chatgpt.md#chatgpt)
