# Find the substring with maximum cost

[Problem link](https://leetcode.com/problems/find-the-substring-with-maximum-cost/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution {
 public:
  int maximumCostSubstring(string s, string chars, vector<int>& vals) {
    unordered_map<char, int> val;
    for (char c = 'a'; c <= 'z'; ++c) val[c] = c - 'a' + 1;
    for (int i = 0; chars[i]; ++i) val[chars[i]] = vals[i];
    int best{};
    for (int i = 0, pref = 0, minpref = 0; s[i]; ++i) {
      best = max(best, (pref += val[s[i]]) - minpref);
      minpref = min(pref, minpref);
    }
    return best;
  }
};
```
## Tags

* [Prefix](/Collections/prefix.md#prefix) > [Sum](/Collections/prefix.md#sum)
