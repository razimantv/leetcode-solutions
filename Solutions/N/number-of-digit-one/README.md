# Number of digit one

[Problem link](https://leetcode.com/problems/number-of-digit-one)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-digit-one

class Solution {
 public:
  int countDigitOne(int n) {
    int ret = 0;
    for (int pos = 1'000'000'000; pos; pos /= 10) {
      if (n < pos) continue;
      int curdig = (n / pos) % 10;
      if (curdig == 0)
        ret += (n / pos / 10) * pos;
      else if (curdig == 1)
        ret += (n / pos / 10) * pos + n % pos + 1;
      else
        ret += (n / pos / 10 + 1) * pos;
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Digits](/Collections/dynamic-programming.md#digits)
