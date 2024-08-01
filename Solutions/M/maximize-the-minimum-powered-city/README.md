# Maximize the minimum powered city

[Problem link](https://leetcode.com/problems/maximize-the-minimum-powered-city/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

class Solution {
 public:
  long long maxPower(vector<int>& stations, int r, int k) {
    int n = stations.size();
    vector<long long> pref0(n + 1);
    for (int i = 0; i < n; ++i) {
      pref0[max(0, i - r)] += stations[i];
      pref0[min(n, i + r + 1)] -= stations[i];
    }
    auto poss = [&](long long x) {
      auto pref = pref0;
      for (long long i = 0, used = 0, psum = 0; i < n; ++i) {
        psum += pref[i];
        long long need = x - psum;
        if (need <= 0) continue;
        if ((used += need) > k) return false;
        pref[i + 1] += need;
        pref[min(i + 2 * r + 1, 0ll + n)] -= need;
      }
      return true;
    };
    long long start = 0, end = 1e11;
    while (end - start > 1) {
      auto mid = (start + end) >> 1;
      (poss(mid) ? start : end) = mid;
    }
    return start;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum) > [For range updates](/Collections/prefix.md#for-range-updates)
* [Greedy](/Collections/greedy.md#greedy)
