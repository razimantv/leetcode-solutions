# Maximum number of events that can be attended

[Problem link](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended

class Solution {
 public:
  int maxEvents(vector<vector<int>>& events) {
    sort(events.begin(), events.end());
    multiset<pair<int, int>> todo;
    int d = 0, ret = 0, i = 0, N = events.size();
    while (1) {
      while (i < N and d >= events[i][0]) {
        todo.insert({events[i][1], events[i][0]});
        ++i;
      }

      if (todo.empty()) {
        if (i == N) break;
        d = events[i][0];
      } else {
        auto [e, s] = *todo.begin();
        todo.erase(todo.begin());
        if (e >= d) ++d, ++ret;
      }
    }
    return ret;
  }
};
```
## Tags

* [Intervals](/Collections/intervals.md#intervals)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
