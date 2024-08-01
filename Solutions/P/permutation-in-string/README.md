# Permutation in string

[Problem link](https://leetcode.com/problems/permutation-in-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/permutation-in-string

class Solution {
 public:
  bool checkInclusion(string s1, string s2) {
    auto &p = s1, &s = s2;
    map<char, int> pcnt, scnt;
    for (char c : p) pcnt[c]++;

    vector<int> ret;
    for (int l = 0, r = 0; r < s.size(); r++) {
      if (++scnt[s[r]] > pcnt[s[r]]) {
        do {
          --scnt[s[l++]];
        } while (scnt[s[r]] > pcnt[s[r]]);
      }
      if (r - l == p.size() - 1) return true;
    }
    return false;
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Sliding window](/Collections/sliding-window.md#sliding-window)
