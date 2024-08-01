# Koko eating bananas

[Problem link](https://leetcode.com/problems/koko-eating-bananas)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/koko-eating-bananas

class Solution {
 public:
  int minEatingSpeed(vector<int>& piles, int h) {
    int low = 0, high = *max_element(piles.begin(), piles.end());
    while (high - low > 1) {
      int mid = (high + low) >> 1;
      long long cur = 0;
      for (int x : piles) cur += x / mid + (x % mid > 0);
      (cur > h ? low : high) = mid;
    }
    return high;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
