# Number of subsequences that satisfy the given sum condition

[Problem link](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution {
 public:
  const int MOD = 1'000'000'007;
  int pow(long long x, int n) {
    int ret{1};
    while (n) {
      if (n & 1) ret = (ret * x) % MOD;
      x = (x * x) % MOD;
      n >>= 1;
    }
    return ret;
  }
  int numSubseq(vector<int>& nums, int target) {
    sort(nums.begin(), nums.end());
    int ret{};
    for (int i = 0, n = nums.size(), j = n - 1; i <= j; ++i) {
      while (j >= i and nums[j] + nums[i] > target) --j;
      if (j < i) break;
      ret += pow(2, j - i);
      if (ret >= MOD) ret -= MOD;
    }
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Modular exponentiation/inverse](/Collections/mathematics.md#modular-exponentiation-inverse)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Two pointers](/Collections/two-pointers.md#two-pointers)
