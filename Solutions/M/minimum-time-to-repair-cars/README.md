# Minimum time to repair cars

[Problem link](https://leetcode.com/problems/minimum-time-to-repair-cars/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution {
 public:
  long long repairCars(vector<int>& ranks, int cars) {
    sort(ranks.begin(), ranks.end());
    auto poss = [&](long long time) {
      long long tot{};
      for (int x : ranks) {
        tot += sqrt(time / x);
        if (tot >= cars) return true;
      }
      return false;
    };

    long long start = 0, end = cars * 100ll * cars;
    while (end - start > 1) {
      auto mid = (end + start) >> 1;
      (poss(mid) ? end : start) = mid;
    }
    return end;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
