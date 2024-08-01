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

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Modular exponentiation/inverse](/Collections/mathematics.md#modular-exponentiation-inverse)
