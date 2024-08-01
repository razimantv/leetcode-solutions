# Capacity to ship packages within d days

[Problem link](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution {
 public:
  int shipWithinDays(vector<int>& weights, int days) {
    int n = weights.size();
    auto poss = [&](int capacity) {
      for (int i = 0, tot = 0, d = 1; i < n; ++i) {
        if (weights[i] > capacity) return false;
        if ((tot += weights[i]) > capacity) {
          tot = weights[i];
          if (++d > days) return false;
        }
      }
      return true;
    };

    int start = *min_element(weights.begin(), weights.end()) - 1,
        end = accumulate(weights.begin(), weights.end(), 0ll);
    while (end - start > 1) {
      int mid = (start + end) >> 1;
      (poss(mid) ? end : start) = mid;
    }
    return end;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
