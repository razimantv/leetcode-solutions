# Sum of floored pairs

[Problem link](https://leetcode.com/problems/sum-of-floored-pairs)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sum-of-floored-pairs

class Solution {
 public:
  int sumOfFlooredPairs(vector<int>& nums) {
    int nmax = *max_element(nums.begin(), nums.end());
    vector<int> cnt(nmax + 1);
    for (int x : nums) cnt[x]++;

    long long ret = 0;
    const int MOD = 1'000'000'007;
    for (int i = 1; i <= nmax; ++i) {
      int x = cnt[i];
      cnt[i] += cnt[i - 1];
      if (x == 0) continue;
      ret = (ret + (x * (long long)x));
      // cout << i << " x" << x << " " << ret << "\n";
      for (int j = 1; j * j <= i; ++j) {
        ret = (ret + ((i / j) * (long long)(cnt[j] - cnt[j - 1]) +
                      j * (long long)(cnt[min(i - 1, i / j)] -
                                      cnt[max(j, i / (j + 1))])) *
                         x);
      }
    }
    return ret % MOD;
    // 16: 1 2 3 4 5-5 6-8 9-16
    // 15: 1 2 3
  }
};
```