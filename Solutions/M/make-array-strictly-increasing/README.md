# Make array strictly increasing

[Problem link](https://leetcode.com/problems/make-array-strictly-increasing/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/make-array-strictly-increasing/

class Solution {
 public:
  int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
    sort(arr2.begin(), arr2.end());
    arr2.erase(unique(arr2.begin(), arr2.end()), arr2.end());
    int m = arr1.size(), n = arr2.size();

    // dp[(i), j] = minimum cost to make first i elements ascending
    //              if ith  element ends up as <= arr2[j].
    //              dp[(i),n] stands for unchanged
    vector<int> dp(n + 1, 1);
    dp[n] = 0;

    for (int i = 1; i < m; ++i) {
      vector<int> newdp(n + 1, m + 1);
      if (arr1[i] > arr1[i - 1]) newdp[n] = dp[n];
      for (int j = 0; j < n; ++j) {
        if (j) newdp[j] = min(newdp[j - 1], dp[j - 1] + 1);
        if (arr1[i - 1] < arr2[j]) newdp[j] = min(newdp[j], dp[n] + 1);
        if (arr1[i] > arr2[j]) newdp[n] = min(newdp[n], dp[j]);
      }
      dp = newdp;
    }
    int ret = *min_element(dp.begin(), dp.end());
    return ret > m ? -1 : ret;
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Array reuse](/Collections/dynamic-programming.md#array-reuse)
* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Element with special meaning](/Collections/dynamic-programming.md#element-with-special-meaning)
