# Time needed to inform all employees

[Problem link](https://leetcode.com/problems/time-needed-to-inform-all-employees/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/time-needed-to-inform-all-employees/

#include <algorithm>
#include <vector>

// ChatGPT solution
class Solution {
 public:
  int dfs(int employee, std::vector<std::vector<int>>& adj_list,
          std::vector<int>& informTime) {
    int max_time = 0;
    for (int subordinate : adj_list[employee]) {
      max_time = std::max(max_time, dfs(subordinate, adj_list, informTime));
    }
    return max_time + informTime[employee];
  }

  int numOfMinutes(int n, int headID, std::vector<int>& manager,
                   std::vector<int>& informTime) {
    std::vector<std::vector<int>> adj_list(n);
    for (int i = 0; i < n; i++) {
      if (manager[i] != -1) {
        adj_list[manager[i]].push_back(i);
      }
    }

    return dfs(headID, adj_list, informTime);
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [ChatGPT](/Collections/chatgpt.md#chatgpt)
