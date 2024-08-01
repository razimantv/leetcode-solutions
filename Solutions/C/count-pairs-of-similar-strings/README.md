# Count pairs of similar strings

[Problem link](https://leetcode.com/problems/count-pairs-of-similar-strings/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/count-pairs-of-similar-strings/

class Solution {
 public:
  int similarPairs(vector<string> &words) {
    map<set<char>, int> cnt;
    for (const auto &w : words) {
      set<char> s;
      for (char c : w) s.insert(c);
      ++cnt[s];
    }

    int ret{};
    for (const auto &[k, v] : cnt) ret += (v * (v - 1)) / 2;
    return ret;
  }
};
```
## Tags

* [Mathematics](/Collections/mathematics.md#mathematics) > [Combinatorics](/Collections/mathematics.md#combinatorics)
* [Hashmap](/Collections/hashmap.md#hashmap)
