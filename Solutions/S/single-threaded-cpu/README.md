# Single threaded cpu

[Problem link](https://leetcode.com/problems/single-threaded-cpu)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/single-threaded-cpu

class Solution {
 public:
  vector<int> getOrder(vector<vector<int>>& tasks) {
    int N = tasks.size();
    for (int i = 0; i < N; ++i) {
      tasks[i].push_back(i);
    }
    sort(tasks.begin(), tasks.end());

    vector<int> ret;
    long long t = 0, i = 0;
    set<pair<int, int>> todo;
    while (i < N or todo.size()) {
      if (!todo.empty()) {
        auto [dt, id] = *todo.begin();
        todo.erase(todo.begin());
        ret.push_back(id);
        t += dt;
      }
      if (i < N and t < tasks[i][0] and todo.empty()) t = tasks[i][0];
      while (i < N and tasks[i][0] <= t) {
        todo.insert({tasks[i][1], tasks[i][2]});
        ++i;
      }
    }
    return ret;
  }
};
```