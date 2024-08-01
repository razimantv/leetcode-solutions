# Kth smallest number in multiplication table

[Problem link](https://leetcode.com/problems/kth-smallest-number-in-multiplication-table)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/kth-smallest-number-in-multiplication-table

class Solution {
 public:
  int findKthNumber(int m, int n, int k) {
    int start = 0, end = m * n;
    while (end - start > 1) {
      int mid = (end + start) >> 1, cur = 0;
      for (int i = 1; i <= m; ++i) cur += min(n, mid / i);
      // cout << mid << ' ' << cur << endl;
      (cur < k ? start : end) = mid;
    }
    return end;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
