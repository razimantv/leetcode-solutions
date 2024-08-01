# String transformation

[Problem link](https://leetcode.com/problems/string-transformation/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/string-transformation/

class Solution {
 public:
  const long long P = 43, MOD = 1'000'000'007;

  vector<vector<long long>> mult(vector<vector<long long>> &m1,
                                 vector<vector<long long>> &m2) {
    vector<vector<long long>> ret(2, vector<long long>(2));
    for (int i = 0; i < 2; ++i)
      for (int j = 0; j < 2; ++j)
        for (int k = 0; k < 2; ++k)
          ret[i][j] = (ret[i][j] + m1[i][k] * m2[k][j]) % MOD;
    return ret;
  }

  pair<long long, long long> dp(long long n, long long k) {
    vector<vector<long long>> ret{{1, 0}, {0, 1}}, mat{{0, n - 1}, {1, n - 2}};
    while (k) {
      if (k & 1) ret = mult(mat, ret);
      mat = mult(mat, mat);
      k >>= 1;
    }
    return {ret[0][0], ret[1][0]};
  }

  int numberOfWays(string s, string t, long long k) {
    int n = s.size();
    vector<long long> pref(n + 1), suf(n + 1);
    long long thash{};
    for (int i = 0; i < n; ++i) {
      pref[i + 1] = (pref[i] * P + s[i] - 'a') % MOD;
      thash = (thash * P + t[i] - 'a') % MOD;
    }

    long long ppow{1};
    for (int i = n - 1; i >= 0; --i) {
      suf[i] = (suf[i + 1] + (s[i] - 'a') * ppow) % MOD;
      ppow = (ppow * P) % MOD;
    }

    int good0{}, good1{};
    ppow = 1;
    for (int i = 0; i < n; ++i) {
      long long cur = (suf[i] * ppow + pref[i]) % MOD;
      if (cur == thash) ++(i ? good1 : good0);
      ppow = (ppow * P) % MOD;
    }

    if (!good0 and !good1) return 0;
    auto [dp0, dp1] = dp(n, k);
    return (dp0 * good0 + dp1 * good1) % MOD;
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Hashing](/Collections/string.md#hashing)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Modular exponentiation/inverse](/Collections/mathematics.md#modular-exponentiation-inverse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Matrix exponentiation](/Collections/dynamic-programming.md#matrix-exponentiation)
