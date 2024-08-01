# Maximize win from two segments

[Problem link](https://leetcode.com/problems/maximize-win-from-two-segments/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximize-win-from-two-segments/

class Solution {
 public:
  int maximizeWin(vector<int>& pos, int k) {
    int n = pos.size();
    if (n < 3) return n;
    vector<int> left(n);
    for (int i = 0, j = 0; i < n; ++i) {
      while (pos[i] - pos[j] > k) ++j;
      left[i] = max((i ? left[i - 1] : 0), i - j + 1);
    }

    int best{};
    for (int i = n - 1, j = i; i; --i) {
      while (pos[j] - pos[i] > k) --j;
      best = max(best, j - i + 1 + left[i - 1]);
    }
    return best;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
* [Array scanning](/Collections/array-scanning.md#array-scanning) > [From both ends of array](/Collections/array-scanning.md#from-both-ends-of-array)
