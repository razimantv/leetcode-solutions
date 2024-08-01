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

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Modular exponentiation/inverse](/Collections/mathematics.md#modular-exponentiation-inverse)
