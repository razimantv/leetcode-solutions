# Process tasks using servers

[Problem link](https://leetcode.com/problems/process-tasks-using-servers)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/process-tasks-using-servers

class Solution {
 public:
  vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
    set<pair<int, int>> free, eventT, eventS;
    for (int i = 0, n = servers.size(); i < n; ++i)
      free.insert({servers[i], i});
    for (int i = 0, n = tasks.size(); i < n; ++i) eventT.insert({i, i});

    vector<int> ret(tasks.size());
    int T = 0;
    while (!eventT.empty()) {
      T = max(T, eventT.begin()->first);
      if (!eventS.empty() and eventS.begin()->first <= T) {
        auto [t, sid] = *eventS.begin();
        eventS.erase(eventS.begin());
        free.insert({servers[sid], sid});
        continue;
      } else if (free.empty()) {
        auto [t, sid] = *eventS.begin();
        eventS.erase(eventS.begin());
        free.insert({servers[sid], sid});
        T = max(T, t);
        continue;
      }

      auto [t, id] = *eventT.begin();
      eventT.erase(eventT.begin());

      auto [w, sid] = *free.begin();
      free.erase(free.begin());
      eventS.insert({T + tasks[id], sid});
      ret[id] = sid;
    }
    return ret;
  }
};
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue)
