# Number of even and odd bits

[Problem link](https://leetcode.com/problems/number-of-even-and-odd-bits/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-even-and-odd-bits/

class Solution {
 public:
  vector<int> evenOddBit(int n) {
    int even{}, odd{};
    while (n) {
      if (n & 1) ++even;
      n >>= 1;
      if (n & 1) ++odd;
      n >>= 1;
    }
    return {even, odd};
  }
};
```
## Tags

* [Bitwise operation](/Collections/bitwise-operation.md#bitwise-operation)
