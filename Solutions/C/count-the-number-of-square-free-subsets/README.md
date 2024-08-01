# Count the number of square free subsets

[Problem link](https://leetcode.com/problems/count-the-number-of-square-free-subsets/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-the-number-of-square-free-subsets/

class Solution {
 public:
  int squareFreeSubsets(vector<int>& nums) {
    vector<int> squarefree(31, 1);
    for (int i : {2, 3, 5})
      for (int j = i * i; j < 31; j += i * i) squarefree[j] = 0;
    vector<int> primes{2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    int P = primes.size(), maskmax = 1 << P;
    vector<int> mask(31);
    for (int i = 2; i < 31; ++i) {
      for (int j = 0; j < P; ++j)
        if (i % primes[j] == 0) mask[i] ^= (1 << j);
    }
    vector<int> DP(maskmax);
    const int MOD = 1'000'000'007;
    DP[0] = 1;
    for (int x : nums) {
      if (!squarefree[x]) continue;
      int m = mask[x];
      for (int i = maskmax - 1; i >= 0; --i)
        if ((i & m) == m) {
          DP[i] += DP[i ^ m];
          if (DP[i] >= MOD) DP[i] -= MOD;
        }
    }

    return accumulate(DP.begin(), DP.end(), -1ll) % MOD;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Subsets](/Collections/dynamic-programming.md#subsets)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Dynamic programming](/Collections/mathematics.md#dynamic-programming)
