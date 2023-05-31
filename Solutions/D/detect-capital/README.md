# Detect capital

[Problem link](https://leetcode.com/problems/detect-capital)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/detect-capital

class Solution {
 public:
  bool detectCapitalUse(string word) {
    int x = 0;
    for (char c : word)
      if (c <= 'Z') ++x;
    return x == 0 or x == word.size() or (x == 1 and word[0] <= 'Z');
  }
};
```
## Tags

* [String](/README.md#String) > [Parsing](/README.md#String-Parsing)
