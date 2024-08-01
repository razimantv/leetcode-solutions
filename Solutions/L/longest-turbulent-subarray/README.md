# Longest turbulent subarray

[Problem link](https://leetcode.com/problems/longest-turbulent-subarray)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-turbulent-subarray

class Solution {
 public:
  int maxTurbulenceSize(vector<int>& arr) {
    int ret = 1;
    for (int i = 1, x = 1, prev = 0, n = arr.size(); i < n; ++i) {
      int cur = 0;
      if (arr[i] > arr[i - 1])
        cur = 1;
      else if (arr[i] < arr[i - 1])
        cur = -1;
      if (!cur)
        x = 1;
      else if (i == 1 or cur == -prev)
        ++x;
      else
        x = 2;
      ret = max(ret, x);
      prev = cur;
    }
    return ret;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
