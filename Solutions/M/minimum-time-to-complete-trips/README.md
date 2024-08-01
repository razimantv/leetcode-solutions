# Minimum time to complete trips

[Problem link](https://leetcode.com/problems/minimum-time-to-complete-trips/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-time-to-complete-trips/

class Solution {
 public:
  long long minimumTime(vector<int>& time, int totalTrips) {
    auto poss = [&](long long t) {
      long long cnt{};
      for (int x : time)
        if ((cnt += t / x) >= totalTrips) return true;
      return false;
    };
    long long start = 0, end = totalTrips * 1ll * time[0];
    while (end - start > 1) {
      long long mid = (end + start) >> 1;
      (poss(mid) ? end : start) = mid;
    }
    return end;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
