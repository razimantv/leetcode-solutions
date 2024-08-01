# 3sum with multiplicity

[Problem link](https://leetcode.com/problems/3sum-with-multiplicity)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/3sum-with-multiplicity

class Solution {
 public:
  int threeSumMulti(vector<int>& arr, int target) {
    vector<int> cnt(101);
    for (int n : arr) ++cnt[n];
    long long ret = 0;
    for (int i = 0; i <= 100 and 3 * i <= target; ++i) {
      if (3 * i == target) {
        ret += (cnt[i] * (long long)(cnt[i] - 1) * (cnt[i] - 2)) / 6;
        break;
      }
      int match = target - 2 * i;
      if (match <= 100)
        ret += cnt[match] * (long long)(cnt[i] * (cnt[i] - 1)) / 2;
      for (int j = i + 1, k = target - i - j; j <= k; ++j, --k) {
        if (k > 100)
          continue;
        else if (j == k)
          ret += cnt[i] * (long long)(cnt[j] * (cnt[j] - 1)) / 2;
        else
          ret += cnt[i] * cnt[j] * cnt[k];
      }
    }
    return ret % 1'000'000'007;
  }
};
```
## Tags

* [Counting elements in array](/Collections/counting-elements-in-array.md#counting-elements-in-array)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
