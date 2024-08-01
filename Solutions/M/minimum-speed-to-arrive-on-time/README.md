# Minimum speed to arrive on time

[Problem link](https://leetcode.com/problems/minimum-speed-to-arrive-on-time)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time

class Solution {
 public:
  bool poss(const vector<int>& dist, double hour, double speed) {
    double t = 0;
    for (int n : dist) {
      if (t - floor(t) > 1e-10) t = floor(t) + 1;
      t += n / speed;
    }
    return t <= hour;
  }

  int minSpeedOnTime(vector<int>& dist, double hour) {
    if (!poss(dist, hour, 2e7)) return -1;
    int start = 0, end = 10'000'000;
    while (end - start > 1) {
      int mid = (start + end) >> 1;
      (poss(dist, hour, mid) ? end : start) = mid;
    }
    return end;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
