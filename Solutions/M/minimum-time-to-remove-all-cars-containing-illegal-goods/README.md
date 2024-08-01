# Minimum time to remove all cars containing illegal goods

[Problem link](https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods

class Solution {
 public:
  int minimumTime(string s) {
    int n = s.size(), prev = 0, ret = n;
    for (int i = 0; i < n; ++i) {
      if (s[i] == '1') prev = min(i + 1, prev + 2);
      ret = min(ret, prev + n - i - 1);
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
