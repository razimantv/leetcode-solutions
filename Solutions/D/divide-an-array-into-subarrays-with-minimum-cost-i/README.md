# Divide an array into subarrays with minimum cost i

[Problem link](https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

class Solution {
 public:
  long long minimumCost(vector<int>& nums) {
    int k = 2;
    set<pair<int, int>> pq, pq2;
    int n = nums.size(), dist = nums.size() - 2;
    long long tot = 0, best = 1ll << 52;
    for (int l = 1, r = 1; r < n; ++r) {
      tot += nums[r];
      pq.insert({-nums[r], r});
      if (pq.size() > k) {
        tot += pq.begin()->first;
        pq2.insert({-pq.begin()->first, pq.begin()->second});
        pq.erase(pq.begin());
      }
      if (pq.size() == k) best = min(best, tot);
      if (r - l == dist) {
        if (pq.count({-nums[l], l})) {
          tot -= nums[l];
          pq.erase({-nums[l], l});
          while (!pq2.empty() and pq2.begin()->second <= l)
            pq2.erase(pq2.begin());
          if (!pq2.empty()) {
            tot += pq2.begin()->first;
            pq.insert({-pq2.begin()->first, pq2.begin()->second});
            pq2.erase(pq2.begin());
          }
        }
        ++l;
      }
    }
    return nums[0] + best;
  }
};
```
## Tags

* [Priority queue](/README.md#Priority_queue) > [K smallest/largest elements](/README.md#Priority_queue-K_smallest_largest_elements) > [Transfer between the two](/README.md#Priority_queue-K_smallest_largest_elements-Transfer_between_the_two)
* [Sliding window](/README.md#Sliding_window)
