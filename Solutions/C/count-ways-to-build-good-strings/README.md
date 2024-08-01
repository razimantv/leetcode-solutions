# Count ways to build good strings

[Problem link](https://leetcode.com/problems/count-ways-to-build-good-strings/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-ways-to-build-good-strings/

inline void add(int &x, int y, int z) {
  x += y;
  if (x >= z) x -= z;
}

class Solution {
 public:
  int countGoodStrings(int low, int high, int zero, int one) {
    const int MOD = 1'000'000'007;
    vector<int> dp(high + 1);
    dp[0] = 1;

    int ret{};
    for (int i = 0; i <= high; ++i) {
      if (i >= low) add(ret, dp[i], MOD);
      if (i + zero <= high) add(dp[i + zero], dp[i], MOD);
      if (i + one <= high) add(dp[i + one], dp[i], MOD);
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming)
