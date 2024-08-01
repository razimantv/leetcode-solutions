# Remove all adjacent duplicates in string ii

[Problem link](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii

class Solution {
 public:
  string removeDuplicates(string s, int k) {
    vector<pair<char, int>> cnt;
    for (char c : s) {
      if (cnt.empty() or cnt.back().first != c)
        cnt.push_back({c, 1});
      else
        cnt.back().second++;
      if (cnt.back().second == k) cnt.pop_back();
    }

    string ret;
    for (auto [c, v] : cnt) ret += string(v, c);
    return ret;
  }
};
```
## Tags

* [Stack](/Collections/stack.md#stack) > [From array elements](/Collections/stack.md#from-array-elements)
