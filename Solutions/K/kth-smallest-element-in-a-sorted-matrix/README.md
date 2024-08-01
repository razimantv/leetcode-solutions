# Kth smallest element in a sorted matrix

[Problem link](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

class Solution {
 public:
  int cnt(const vector<vector<int>>& matrix, int n, int x) {
    int pos =
        upper_bound(matrix[0].begin(), matrix[0].end(), x) - matrix[0].begin();
    if (!pos) return 0;
    int ret = pos;
    for (int i = 1; i < n; ++i) {
      while (pos > 0 and matrix[i][pos - 1] > x) --pos;
      ret += pos;
      if (!pos) return ret;
    }
    return ret;
  }
  int kthSmallest(vector<vector<int>>& matrix, int k) {
    int n = matrix.size(), start = matrix[0][0] - 1, end = matrix[n - 1][n - 1],
        mid;
    while (end - start > 1)
      mid = start + ((end - start) >> 1),
      (cnt(matrix, n, mid) >= k ? end : start) = mid;
    return end;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
