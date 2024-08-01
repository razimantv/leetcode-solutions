# Longest substring of all vowels in order

[Problem link](https://leetcode.com/problems/longest-substring-of-all-vowels-in-order)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-substring-of-all-vowels-in-order

class Solution {
 public:
  int longestBeautifulSubstring(string word) {
    int n = word.size(), best = 0;
    for (int i = 0; i < n;) {
      while (i < n and word[i] != 'a') ++i;
      int j = i + 1;
      set<char> seen{'a'};
      while (j < n and word[j] >= word[j - 1]) {
        seen.insert(word[j++]);
      }
      if (seen.size() == 5) best = max(best, j - i);
      i = j;
    }
    return best;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [Contiguous region](/Collections/array-scanning.md#contiguous-region)
