# Maximum running time of n computers

[Problem link](https://leetcode.com/problems/maximum-running-time-of-n-computers/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-running-time-of-n-computers/

class Solution {
 public:
  bool work(vector<int>& ar, long long target, int n) {
    long long tot{};
    for (long long x : ar) tot += min(x, target);
    return tot >= target * n;
  }
  long long maxRunTime(int n, vector<int>& batteries) {
    long long start = 0,
              end = accumulate(batteries.begin(), batteries.end(), 0ll) / n + 1;
    while (end - start > 1) {
      auto mid = (end + start) / 2;
      (work(batteries, mid, n) ? start : end) = mid;
    }
    return start;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
