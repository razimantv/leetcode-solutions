# Nth magical number

[Problem link](https://leetcode.com/problems/nth-magical-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/nth-magical-number

class Solution {
 public:
  int nthMagicalNumber(long long n, long long a, long long b) {
    long long l = a * b / gcd(a, b);

    long long start = 0, end = n * max(a, b);
    while (end - start > 1) {
      auto mid = (start + end) >> 1;
      auto cur = mid / a + mid / b - mid / l;
      ((cur < n) ? start : end) = mid;
    }
    return end % 1'000'000'007;
  }
};
```
## Tags

* [Binary search](/README.md#Binary_search)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Basic](/README.md#Mathematics-Number_theory-Basic)
