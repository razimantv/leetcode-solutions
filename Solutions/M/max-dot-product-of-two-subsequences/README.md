# Max dot product of two subsequences

[Problem link](https://leetcode.com/problems/max-dot-product-of-two-subsequences)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/max-dot-product-of-two-subsequences

class Solution {
 public:
  int maxDotProduct(vector<int>& nums1, vector<int>& nums2) {
    int M = nums1.size(), N = nums2.size();
    vector<vector<int>> best(M + 1, vector<int>(N + 1, 0));
    best[1][1] = nums1[0] * nums2[0];
    for (int i = 1; i < M; i++)
      best[i + 1][1] = max(nums1[i] * nums2[0], best[i][1]);
    for (int i = 1; i < N; i++)
      best[1][i + 1] = max(nums1[0] * nums2[i], best[1][i]);
    for (int i = 1; i < M; i++)
      for (int j = 1; j < N; j++)
        best[i + 1][j + 1] = max(nums1[i] * nums2[j] + max(0, best[i][j]),
                                 max(best[i][j + 1], best[i + 1][j]));
    return best[M][N];
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Longest common subsequence](/Collections/dynamic-programming.md#longest-common-subsequence)
