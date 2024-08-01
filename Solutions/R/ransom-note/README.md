# Ransom note

[Problem link](https://leetcode.com/problems/ransom-note)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/ransom-note

class Solution {
 public:
  bool canConstruct(string ransomNote, string magazine) {
    map<char, int> cnt;
    for (char c : magazine) cnt[c]++;
    for (char c : ransomNote)
      if (cnt[c]-- == 0) return false;
    return true;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
