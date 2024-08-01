# Longest substring without repeating characters

[Problem link](https://leetcode.com/problems/longest-substring-without-repeating-characters)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-substring-without-repeating-characters

class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    int best = 0;
    unordered_set<char> seen;
    for (int i = 0, j = 0, n = s.size(); i < n; ++i) {
      while (seen.count(s[i])) seen.erase(s[j++]);
      best = max(best, i - j + 1);
      seen.insert(s[i]);
    }
    return best;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
* [Unique elements in subarray](/Collections/unique-elements-in-subarray.md#unique-elements-in-subarray)
