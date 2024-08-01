# Maximize value of function in a ball passing game

[Problem link](https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximize-value-of-function-in-a-ball-passing-game/

class Solution {
 public:
  long long getMaxFunctionValue(vector<int>& receiver, long long k) {
    int n = receiver.size();

    vector<vector<int>> rec{receiver};
    vector<vector<long long>> recsum{{}};
    for (int x : receiver) recsum[0].push_back(x);

    for (long long kk = 2; kk <= k; kk <<= 1) {
      vector<int> newrec(n);
      vector<long long> newrecsum(n);
      for (int i = 0; i < n; ++i) {
        int ii = rec.back()[i];
        newrec[i] = rec.back()[ii];
        newrecsum[i] = recsum.back()[i] + recsum.back()[ii];
      }
      rec.push_back(newrec);
      recsum.push_back(newrecsum);
    }

    long long best{};
    for (int i = 0; i < n; ++i) {
      int x{i};
      long long cur{x};
      for (int j = 0; j < 40; ++j) {
        if (k & (1ll << j)) {
          cur += recsum[j][x];
          x = rec[j][x];
        }
      }
      best = max(best, cur);
    }
    return best;
  }
};
```
## Tags

* [Binary lifting](/Collections/binary-lifting.md#binary-lifting)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Binary lifting](/Collections/dynamic-programming.md#binary-lifting)
