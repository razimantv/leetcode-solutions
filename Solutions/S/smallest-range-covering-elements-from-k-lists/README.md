# Smallest range covering elements from k lists

[Problem link](https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists

class Solution {
 public:
  vector<int> smallestRange(vector<vector<int>>& nums) {
    int n = nums.size();
    auto cmp = [&](const pair<int, int>& a, const pair<int, int>& b) {
      if (nums[a.first][a.second] != nums[b.first][b.second])
        return nums[a.first][a.second] < nums[b.first][b.second];
      return a < b;
    };

    set<pair<int, int>, decltype(cmp)> heap(cmp);
    for (int i = 0; i < n; ++i) heap.insert({i, 0});

    vector<int> best{-1'000'000, 1'000'000};
    while (heap.size() == n) {
      auto [lid, lpos] = *heap.begin();
      auto [rid, rpos] = *heap.rbegin();
      int l = nums[lid][lpos], r = nums[rid][rpos];
      if (r - l < best[1] - best[0] or
          (r - l == best[1] - best[0] and l < best[0]))
        best = {l, r};
      heap.erase(heap.begin());
      if (++lpos < nums[lid].size()) heap.insert({lid, lpos});
    }

    return best;
  }
};
```