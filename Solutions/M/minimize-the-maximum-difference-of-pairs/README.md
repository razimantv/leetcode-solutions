# Minimize the maximum difference of pairs

[Problem link](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/

class Solution {
 public:
  int minimizeMax(vector<int>& nums, int p) {
    if (!p) return 0;
    int n = nums.size();
    sort(nums.begin(), nums.end());
    int start{INT_MAX}, end{};
    for (int i = n; --i;) {
      end = max(end, nums[i] -= nums[i - 1]);
      start = min(start, nums[i]);
    }

    auto poss = [&](int x) {
      for (int i = 1, prev = 0, cnt = 0; i < n; ++i) {
        if (!prev and nums[i] <= x) {
          if (++cnt == p) return true;
          prev = 1;
        } else
          prev = 0;
      }
      return false;
    };

    --start;
    while (end - start > 1) {
      int mid = (start + end) >> 1;
      (poss(mid) ? end : start) = mid;
    }

    return end;
  }
};
```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search)
* [Greedy](/Collections/greedy.md#greedy)
