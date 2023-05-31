# Valid anagram

[Problem link](https://leetcode.com/problems/valid-anagram)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/valid-anagram

class Solution {
 public:
  bool isAnagram(string s, string t) {
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());
    return s == t;
  }
};
```