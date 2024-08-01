# Minimum time to complete all tasks

[Problem link](https://leetcode.com/problems/minimum-time-to-complete-all-tasks/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-time-to-complete-all-tasks/

class Solution {
 public:
  int findMinimumTime(vector<vector<int>>& tasks) {
    sort(tasks.begin(), tasks.end(),
         [](vector<int>& t1, vector<int>& t2) { return t1[1] < t2[1]; });

    vector<int> used(2001);
    int ret{};
    for (auto& t : tasks) {
      for (int i = t[0]; i <= t[1]; ++i)
        if (used[i] and !--t[2]) break;
      for (int i = t[1]; t[2]; --i)
        if (!used[i]) {
          used[i] = 1;
          ++ret;
          --t[2];
        }
    }
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Intervals](/Collections/intervals.md#intervals) > [Overlap](/Collections/intervals.md#overlap)
