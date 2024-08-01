# Longest word in dictionary

[Problem link](https://leetcode.com/problems/longest-word-in-dictionary)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-word-in-dictionary

class Solution {
 public:
  string longestWord(vector<string>& words) {
    unordered_set<string> s;
    for (const auto& w : words) s.insert(w);

    string best = "";
    for (const auto& w : words) {
      if (w.size() < best.size() or (w.size() == best.size() and best < w))
        continue;
      for (int i = 1, L = w.size(); i <= L; ++i)
        if (!s.count(w.substr(0, i))) goto BPP;
      best = w;
    BPP:;
    }
    return best;
  }
};
```
## Tags

* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
* [Hashmap](/Collections/hashmap.md#hashmap)
