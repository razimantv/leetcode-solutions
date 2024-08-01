# Maximum number of achievable transfer requests

[Problem link](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/

class Solution {
 public:
  int maximumRequests(int n, vector<vector<int>>& requests) {
    int l = requests.size(), ret{};
    for (int mask = 1; mask < (1 << l); ++mask) {
      int bits = __builtin_popcount(mask);
      if (bits <= ret) continue;
      vector<int> delta(n);
      int bad{};
      for (int i = 0; i < l; ++i) {
        if (!(mask & (1 << i))) continue;
        int after = ++delta[requests[i][0]];
        bad += (after == 1) - (after == 0);
        after = --delta[requests[i][1]];
        bad += (after == -1) - (after == 0);
      }
      if (!bad) ret = bits;
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Brute force enumeration](/Collections/brute-force-enumeration.md#brute-force-enumeration) > [Combinatorial](/Collections/brute-force-enumeration.md#combinatorial)
