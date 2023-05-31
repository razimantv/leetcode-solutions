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

* [Sliding window](/README.md#Sliding_window)
* [Array scanning](/README.md#Array_scanning) > [From both ends of array](/README.md#Array_scanning-From_both_ends_of_array)
