# Minimize the maximum of two arrays

[Problem link](https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimize-the-maximum-of-two-arrays/

class Solution {
 public:
  int minimizeSet(int d1, int d2, int cnt1, int cnt2) {
    long long l = d1 * (long long)(d2 / __gcd(d1, d2)), target = cnt1 + cnt2;
    auto good = [&](int n) {
      int n1 = n / d2 - n / l;
      int n2 = n / d1 - n / l;
      int n12 = n - n1 - n2 - n / l;
      return min(cnt1, n1) + min(cnt2, n2) + n12;
    };

    int ret = target;
    while (1) {
      auto add = target - good(ret);
      if (!add) break;
      ret += add;
    }
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
* [Search by iterative bound improvement](/Collections/search-by-iterative-bound-improvement.md#search-by-iterative-bound-improvement)
