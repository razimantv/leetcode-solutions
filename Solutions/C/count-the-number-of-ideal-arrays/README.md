# Count the number of ideal arrays

[Problem link](https://leetcode.com/problems/count-the-number-of-ideal-arrays)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-the-number-of-ideal-arrays

class Solution {
 public:
  vector<int> cache;
  const int MOD = 1'000'000'007;

  long long modpow(long long n, int k) {
    long long ret = 1;
    while (k) {
      if (k & 1) ret = (ret * n) % MOD;
      n = (n * n) % MOD;
      k >>= 1;
    }
    return ret;
  }
  int inv(int n) { return modpow(n, MOD - 2); }
  int work(int cnt, int n) {
    // a1 + a2 + … an = cnt
    //  ans = (cnt + n-1) choose cnt
    if (cnt < cache.size()) return cache[cnt];
    long long ret = 1;
    for (int i = 0; i < cnt; ++i) {
      ret = (ret * (cnt + n - 1 - i)) % MOD;
      ret = (ret * inv(i + 1)) % MOD;
    }
    cache.push_back(ret);
    return ret;
  }
  int idealArrays(int n, int maxValue) {
    vector<int> aprime(maxValue + 1);
    for (int i = 2; i * i <= maxValue; ++i) {
      if (!aprime[i])
        for (int j = i * i; j <= maxValue; j += i) aprime[j] = i;
    }

    cache = {1};
    long long ret = 1;

    vector<unordered_map<int, int>> pcnt(maxValue + 1);

    for (int i = 2; i <= maxValue; ++i) {
      long long cur = 1;
      if (!aprime[i])
        pcnt[i][i] = 1;
      else {
        pcnt[i] = pcnt[i / aprime[i]];
        ++pcnt[i][aprime[i]];
      }
      for (auto [k, v] : pcnt[i]) cur = (cur * work(v, n)) % MOD;
      ret = (ret + cur) % MOD;
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/README.md#Dynamic_programming) > [Number theory](/README.md#Dynamic_programming-Number_theory)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Modular exponentiation/inverse](/README.md#Mathematics-Number_theory-Modular_exponentiation_inverse)
* [Mathematics](/README.md#Mathematics) > [Number theory](/README.md#Mathematics-Number_theory) > [Prime sieving](/README.md#Mathematics-Number_theory-Prime_sieving)
