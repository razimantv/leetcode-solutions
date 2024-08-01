# Count anagrams

[Problem link](https://leetcode.com/problems/count-anagrams/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-anagrams/

class Solution {
 public:
  const int MOD = 1'000'000'007;

  long long factorial(int n) {
    long long ret{1};
    for (int i = 1; i <= n; ++i) ret = (ret * i) % MOD;
    return ret;
  }

  long long inverse(long long n) {
    long long ret{1};
    for (long long b = MOD - 2; b; b >>= 1) {
      if (b & 1) ret = (ret * n) % MOD;
      n = (n * n) % MOD;
    }
    return ret;
  }
  long long permutations(string s) {
    unordered_map<char, int> cnt;
    int all{};
    for (char c : s) ++cnt[c], ++all;

    long long ret = factorial(all);
    for (auto [k, v] : cnt) ret = (ret * inverse(factorial(v))) % MOD;
    return ret;
  }
  int countAnagrams(string s) {
    istringstream iss(s);
    int ret{1};
    string temp;
    while (iss >> temp) ret = (ret * permutations(temp)) % MOD;
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Closed form expressions](/Collections/mathematics.md#closed-form-expressions)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Modular exponentiation/inverse](/Collections/mathematics.md#modular-exponentiation-inverse)
* [String](/Collections/string.md#string) > [Parsing](/Collections/string.md#parsing)
* [Hashmap](/Collections/hashmap.md#hashmap)
