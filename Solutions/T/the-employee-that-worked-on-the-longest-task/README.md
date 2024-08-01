# The employee that worked on the longest task

[Problem link](https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/the-employee-that-worked-on-the-longest-task/

class Solution {
 public:
  int hardestWorker(int n, vector<vector<int>>& logs) {
    int best = 0, bestval = 0;
    for (int i = 0, t = 0; i < logs.size(); ++i) {
      int curval = logs[i][1] - t;
      if (curval > bestval or (curval == bestval and logs[i][0] < best))
        bestval = curval, best = logs[i][0];
      t = logs[i][1];
    }
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning)
* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
