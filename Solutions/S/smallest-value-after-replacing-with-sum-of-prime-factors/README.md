# Smallest value after replacing with sum of prime factors

[Problem link](https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

class Solution {
 public:
  int smallestValue(int n) {
    int x{}, nn = n;
    for (int p = 2; p * p <= n; ++p) {
      while (!(n % p)) n /= p, x += p;
    }
    if (n > 1) x += n;
    return x == nn ? x : smallestValue(x);
  }
};
```
## Tags

* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Factor listing in sqrt(N)](/README.md#Mathematics-Number_theory-Factor_listing_in_sqrt_N_)
