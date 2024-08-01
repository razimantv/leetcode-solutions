# Minimum total cost to make arrays unequal

[Problem link](https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/

class Solution {
 public:
  long long minimumTotalCost(vector<int>& nums1, vector<int>& nums2) {
    int n = nums1.size();
    unordered_map<int, int> all, bad;
    int worst = -1, swaps{};
    long long ret{};
    for (int i = 0; i < n; ++i) {
      if (++all[nums1[i]] > n or ++all[nums2[i]] > n) return -1;
      if (nums1[i] == nums2[i]) {
        ++swaps;
        ret += i;
        if (++bad[nums1[i]] > bad[worst]) worst = nums1[i];
      }
    }

    for (int i = 0, target = 2 * bad[worst]; i < n and swaps < target; ++i) {
      if (nums1[i] != worst and nums2[i] != worst and nums1[i] != nums2[i])
        ++swaps, ret += i;
    }
    return ret;
  }
};
```
## Tags

* [Greedy](/Collections/greedy.md#greedy)
* [Hashmap](/Collections/hashmap.md#hashmap)
