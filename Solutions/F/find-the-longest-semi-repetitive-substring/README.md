# Find the longest semi repetitive substring

[Problem link](https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-longest-semi-repetitive-substring/

class Solution {
 public:
  int longestSemiRepetitiveSubstring(string s) {
    int best{1};
    for (int i = 1, p1 = 0, p2 = 0; s[i]; ++i) {
      if (s[i] == s[i - 1]) p1 = p2, p2 = i;
      best = max(best, i - p1 + 1);
    }
    return best;
  }
};
```
## Tags

* [Two pointers](/Collections/two-pointers.md#two-pointers)
