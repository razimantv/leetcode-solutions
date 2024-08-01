# Non negative integers without consecutive ones

[Problem link](https://leetcode.com/problems/non-negative-integers-without-consecutive-ones)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/non-negative-integers-without-consecutive-ones

class Solution {
 public:
  int findIntegers(int n) {
    vector<int> cnt[2]{{1}, {1}};
    vector<int> bin;
    for (int nn = n, z = 1, o = 1; nn; nn >>= 1) {
      int cur = nn & 1;
      bin.push_back(cur);
      swap(z, o);
      z += o;
      cnt[0].push_back(z);
      cnt[1].push_back(o);
    }

    reverse(bin.begin(), bin.end());
    int ret = 0;
    for (int i = 0, prev = 0, m = bin.size(); i < m; ++i) {
      if (bin[i] == 0)
        prev = 0;
      else {
        ret += cnt[0][m - i - 1];
        if (prev and bin[i]) break;
        prev = bin[i];
      }
      if (i == m - 1) ++ret;
    }
    return ret;
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Digits](/Collections/dynamic-programming.md#digits)
