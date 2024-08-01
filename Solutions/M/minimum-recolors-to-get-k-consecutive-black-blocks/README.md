# Minimum recolors to get k consecutive black blocks

[Problem link](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks

class Solution {
 public:
  int minimumRecolors(string blocks, int k) {
    int n = blocks.size(), best = k;
    for (int i = 0, cnt = 0; i < n; ++i) {
      cnt += (blocks[i] == 'B');
      if (i >= k) cnt -= (blocks[i - k] == 'B');
      if (i >= k - 1) best = min(best, k - cnt);
    }
    return best;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
