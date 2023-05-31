# Count good numbers

[Problem link](https://leetcode.com/problems/count-good-numbers)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-good-numbers

class Solution {
 public:
  const long long MOD = 1'000'000'007;
  long long mpow(long long a, long long b) {
    long long ret = 1;
    while (b) {
      if (b & 1) ret = (ret * a) % MOD;
      a = (a * a) % MOD;
      b >>= 1;
    }
    return ret;
  }
  int countGoodNumbers(long long n) {
    long long odd = n >> 1, even = n - odd;
    return (mpow(4, odd) * mpow(5, even)) % MOD;
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Modular exponentiation/inverse](/README.md#Mathematics-Number_theory-Modular_exponentiation_inverse)
