# Maximum element sum of a complete subset of indices

[Problem link](https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-element-sum-of-a-complete-subset-of-indices/

class Solution {
 public:
  long long maximumSum(vector<int>& nums) {
    int n = nums.size();
    vector<int> left(n + 1);
    iota(left.begin(), left.end(), 0);
    for (int i = 2; i * i <= n; ++i) {
      if (left[i] != i) continue;
      for (int sq = i * i, j = sq; j <= n; j += sq) {
        while (left[j] % sq == 0) left[j] /= sq;
      }
    }

    unordered_map<int, long long> tot;
    long long ret{};
    for (int i = 0; i < n; ++i) {
      ret = max(ret, tot[left[i + 1]] += nums[i]);
    }
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Basic](/Collections/mathematics.md#basic)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Number theory](/Collections/mathematics.md#number-theory) > [Prime sieving](/Collections/mathematics.md#prime-sieving)
