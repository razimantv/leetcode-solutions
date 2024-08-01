# Get maximum in generated array

[Problem link](https://leetcode.com/problems/get-maximum-in-generated-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/get-maximum-in-generated-array

class Solution {
 public:
  int getMaximumGenerated(int n) {
    if (n == 0) return 0;
    vector<int> ar(n + 1);
    int ret = ar[1] = 1;
    for (int i = 2; i <= n; ++i) {
      if (i & 1)
        ar[i] = ar[i / 2] + ar[i - i / 2];
      else
        ar[i] = ar[i / 2];
      ret = max(ret, ar[i]);
    }
    return ret;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
