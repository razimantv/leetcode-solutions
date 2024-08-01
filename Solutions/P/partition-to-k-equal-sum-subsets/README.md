# Partition to k equal sum subsets

[Problem link](https://leetcode.com/problems/partition-to-k-equal-sum-subsets)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets

class Solution {
 public:
  set<vector<int>> seen;
  bool work(const vector<int>& nums, int n, int k, int i, vector<int>& cur,
            int target) {
    if (i == n) return cur[0] == cur.back();
    if (seen.count(cur)) return false;
    seen.insert(cur);

    for (int j = 0; j < k; ++j) {
      if (cur[j] + nums[i] <= target) {
        auto temp = cur;
        temp[j] += nums[i];
        sort(temp.begin(), temp.end());

        if (work(nums, n, k, i + 1, temp, target)) return true;
      }
    }
    return false;
  }

  bool canPartitionKSubsets(vector<int>& nums, int k) {
    if (k == 1) return true;
    int tot = accumulate(nums.begin(), nums.end(), 0);
    if (tot % k) return false;

    vector<int> temp(k);
    sort(nums.begin(), nums.end(), greater<int>());
    return work(nums, nums.size(), k, 0, temp, tot / k);
  }
};
```
## Tags

* [Dynamic programming](/Collections/dynamic-programming.md#dynamic-programming) > [Memoised recursion](/Collections/dynamic-programming.md#memoised-recursion)
* [Backtracking](/Collections/backtracking.md#backtracking)
