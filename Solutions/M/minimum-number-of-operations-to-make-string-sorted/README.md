# Minimum number of operations to make string sorted

[Problem link](https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-number-of-operations-to-make-string-sorted

class Solution {
 public:
  const long long MOD = 1'000'000'007;
  long long modpow(long long a, long long b) {
    long long ret = 1;
    while (b) {
      if (b & 1) ret = (ret * a) % MOD;
      a = (a * a) % MOD;
      b >>= 1;
    }
    return ret;
  }

  long long inv(long long n) { return modpow(n, MOD - 2); }

  int makeStringSorted(string s) {
    vector<int> cnt(26, 0);
    int tot = 0;
    for (char c : s) cnt[c - 'a']++, tot++;
    long long ret = 0;
    vector<long long> factorial(tot + 1, 1), invfac(tot + 1, 1);
    for (int i = 2; i <= tot; ++i) {
      factorial[i] = (factorial[i - 1] * i) % MOD;
      invfac[i] = inv(factorial[i]);
    }

    for (char c : s) {
      c -= 'a';
      for (int i = 0; i < c; ++i) {
        if (!cnt[i]) continue;
        long long cur = factorial[tot - 1];
        for (int j = 0; j < 26; ++j) {
          if (i == j)
            cur = (cur * invfac[cnt[j] - 1]) % MOD;
          else
            cur = (cur * invfac[cnt[j]]) % MOD;
        }
        ret = (ret + cur) % MOD;
      }
      --tot;
      --cnt[c];
    }
    return ret;
  }
};
```
## Tags

* [Permutation](/Collections/permutation.md#permutation) > [Next/Previous](/Collections/permutation.md#next-previous)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Modular exponentiation/inverse](/Collections/mathematics.md#modular-exponentiation-inverse)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
