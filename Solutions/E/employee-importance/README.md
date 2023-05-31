# Employee importance

[Problem link](https://leetcode.com/problems/employee-importance)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/employee-importance

/*
// Definition for Employee.
class Employee {
public:
    int id;
    int importance;
    vector<int> subordinates;
};
*/

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

* [Graph theory](/README.md#Graph_theory) > [Depth first search](/README.md#Graph_theory-Depth_first_search)
* [Dynamic programming](/README.md#Dynamic_programming) > [Trees](/README.md#Dynamic_programming-Trees)
