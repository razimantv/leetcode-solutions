# Count collisions of monkeys on a polygon

[Problem link](https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-collisions-of-monkeys-on-a-polygon/

class Solution {
 public:
  const int MOD = 1'000'000'007;
  long long pow(long long a, int b) {
    long long ret = 1;
    while (b) {
      if (b & 1) ret = (ret * a) % MOD;
      a = (a * a) % MOD;
      b >>= 1;
    }
    return ret;
  }
  int monkeyMove(int n) { return (pow(2, n) + MOD - 2) % MOD; }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Modular exponentiation/inverse](/README.md#Mathematics-Number_theory-Modular_exponentiation_inverse)
