# Longest consecutive sequence

[Problem link](https://leetcode.com/problems/longest-consecutive-sequence)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-consecutive-sequence

class Solution {
 public:
  int longestConsecutive(vector<int>& nums) {
    unordered_set<int> s;
    for (int n : nums) s.insert(n);

    int best = 0;
    while (!s.empty()) {
      int x = *s.begin();
      s.erase(s.begin());

      int cnt = 1;
      for (int i = x - 1;; --i) {
        if (!s.count(i)) break;
        ++cnt;
        s.erase(i);
      }
      for (int i = x + 1;; ++i) {
        if (!s.count(i)) break;
        ++cnt;
        s.erase(i);
      }
      best = max(best, cnt);
    }
    return best;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
