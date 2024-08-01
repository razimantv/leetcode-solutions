# Find the longest equal subarray

[Problem link](https://leetcode.com/problems/find-the-longest-equal-subarray/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-longest-equal-subarray/

class Solution {
 public:
  int longestEqualSubarray(vector<int>& nums, int k) {
    int ret{1};
    unordered_map<int, int> cnt;
    map<int, unordered_set<int>, greater<int>> cntmap;
    for (int l = 0, r = 0, n = nums.size(); r < n; ++r) {
      int x = nums[r], cx = 0;
      if (cnt.count(x)) {
        cx = cnt[x];
        cntmap[cx].erase(x);
        if (cntmap[cx].empty()) cntmap.erase(cx);
      }

      cnt[x] = ++cx;
      cntmap[cx].insert(x);

      int maxcnt = cntmap.begin()->first;
      while (maxcnt + k < r - l + 1) {
        int y = nums[l], cy = cnt[y];
        cntmap[cy].erase(y);
        if (cntmap[cy].empty()) cntmap.erase(cy);

        if (!(cnt[y] = --cy)) {
          cnt.erase(y);
        } else {
          cntmap[cy].insert(y);
        }

        maxcnt = cntmap.begin()->first;
        ++l;
      }

      ret = max(ret, maxcnt);
    }
    return ret;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Forward and backward](/Collections/hashmap.md#forward-and-backward)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Group items](/Collections/hashmap.md#group-items)
