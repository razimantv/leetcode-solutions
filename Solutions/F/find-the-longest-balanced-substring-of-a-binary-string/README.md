# Find the longest balanced substring of a binary string

[Problem link](https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/

class Solution {
 public:
  int findTheLongestBalancedSubstring(string s) {
    int best{};
    for (int i = 0; s[i];) {
      while (s[i] == '1') ++i;
      int j = i;
      while (s[j] == '0') ++j;
      int k = j;
      while (s[k] == '1') ++k;
      best = max(best, min(j - i, k - j));
      i = k;
    }
    return best * 2;
  }
};
```
## Tags

* [Array scanning](/README.md#Array_scanning) > [Contiguous region](/README.md#Array_scanning-Contiguous_region)
