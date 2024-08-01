# Redistribute characters to make all strings equal

[Problem link](https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal

class Solution {
 public:
  bool makeEqual(vector<string>& words) {
    int N = words.size();
    vector<int> cnt(26);
    for (auto& s : words)
      for (char c : s) ++cnt[c - 'a'];
    for (int x : cnt)
      if (x % N) return false;
    return true;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
