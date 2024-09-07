# Employee importance

[Problem link](https://leetcode.com/problems/employee-importance)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/employee-importance


class Solution {
 public:
  unordered_map<int, Employee*> danger;

  int dfs(Employee* e) {
    int cur = e->importance;
    for (int s : e->subordinates) cur += dfs(danger[s]);
    return cur;
  }
  int getImportance(vector<Employee*> employees, int id) {
    for (auto e : employees) danger[e->id] = e;
    return dfs(danger[id]);
  }
};
```
## Tags

* [Graph theory](/Collections/graph-theory.md#graph-theory) > [Depth first search](/Collections/graph-theory.md#depth-first-search)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Trees](/Collections/dynamic-programming.md#trees)
