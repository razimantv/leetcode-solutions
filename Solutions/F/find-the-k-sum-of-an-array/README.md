# Find the k sum of an array

[Problem link](https://leetcode.com/problems/find-the-k-sum-of-an-array)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-k-sum-of-an-array

class Solution {
 public:
  long long kSum(vector<int>& nums, int k) {
    long long tot{};
    for (int& x : nums)
      if (x >= 0)
        tot += x;
      else
        x = -x;
    if (k == 1) return tot;

    int n = nums.size();
    sort(nums.begin(), nums.end());
    multiset<pair<long long, int>> sum;
    sum.insert({nums[0] - tot, 0});
    for (int i = 1; i < k; ++i) {
      tot = sum.begin()->first;
      int pos = sum.begin()->second;
      sum.erase(sum.begin());

      if (pos < n - 1) {
        sum.insert({tot + nums[pos + 1], pos + 1});
        sum.insert({tot + nums[pos + 1] - nums[pos], pos + 1});
      }
    }
    return -tot;
  }
};
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Dijkstra-like processing of subarrays](/Collections/priority-queue.md#dijkstra-like-processing-of-subarrays)
