# Find all anagrams in a string

[Problem link](https://leetcode.com/problems/find-all-anagrams-in-a-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-all-anagrams-in-a-string

class Solution {
 public:
  vector<int> findAnagrams(string s, string p) {
    map<char, int> pcnt, scnt;
    for (char c : p) pcnt[c]++;

    vector<int> ret;
    for (int l = 0, r = 0; r < s.size(); r++) {
      if (++scnt[s[r]] > pcnt[s[r]]) {
        do {
          --scnt[s[l++]];
        } while (scnt[s[r]] > pcnt[s[r]]);
      }
      if (r - l == p.size() - 1) ret.push_back(l);
    }
    return ret;
  }
};
```
## Tags

* [Counting elements in array](/Collections/counting-elements-in-array.md#counting-elements-in-array)
* [Sliding window](/Collections/sliding-window.md#sliding-window)
