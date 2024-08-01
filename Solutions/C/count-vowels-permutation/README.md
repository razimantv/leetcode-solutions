# Count vowels permutation

[Problem link](https://leetcode.com/problems/count-vowels-permutation)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-vowels-permutation

class Solution {
 public:
  int countVowelPermutation(int n) {
    long long a = 1, e = 1, i = 1, o = 1, u = 1;
    const long long MOD = 1'000'000'007;
    while (--n) {
      long long newa = e, newe = (a + i) % MOD, newi = (a + e + o + u) % MOD,
                newo = (i + u) % MOD, newu = a % MOD;
      a = newa, e = newe, i = newi, o = newo, u = newu;
    }
    return (a + e + i + o + u) % MOD;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
