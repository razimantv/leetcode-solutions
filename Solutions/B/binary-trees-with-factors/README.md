# Binary trees with factors

[Problem link](https://leetcode.com/problems/binary-trees-with-factors)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/binary-trees-with-factors

class Solution {
 public:
  int N;
  static const int MOD = 1'000'000'007;
  int numFactoredBinaryTrees(vector<int>& arr) {
    int N = arr.size();
    vector<int> DP(N);
    sort(arr.begin(), arr.end());

    int ret = 0;
    for (int i = 0; i < N; ++i) {
      DP[i] = 1;
      for (int j = 0, k = i - 1; j <= k;) {
        if (arr[j] * (long long)arr[k] > arr[i])
          --k;
        else if (arr[j] * (long long)arr[k] == arr[i]) {
          DP[i] = (DP[i] + (2 - (j == k)) * DP[j] * (long long)DP[k]) % MOD;
          ++j;
        } else
          ++j;
      }
      ret = (ret + DP[i]) % MOD;
    }
    return ret;
  }
};
```
## Tags

* [Dynamic programming](/README.md#Dynamic_programming)
* [Mathematics](/README.md#Mathematics) > [Combinatorics](/README.md#Mathematics-Combinatorics)
* [Sliding window](/README.md#Sliding_window)
