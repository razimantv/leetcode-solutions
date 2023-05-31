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

* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
* [Search by iterative bound improvement](/README.md#Search_by_iterative_bound_improvement)
