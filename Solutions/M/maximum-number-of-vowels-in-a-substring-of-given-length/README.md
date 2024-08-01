# Maximum number of vowels in a substring of given length

[Problem link](https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution {
 public:
  int maxVowels(string s, int k) {
    int ret{};
    string vowels = "aeiou";
    unordered_set<char> vset(vowels.begin(), vowels.end());
    for (int i = 0, n = s.size(), v = 0; i < n; ++i) {
      if (i >= k) v -= vset.count(s[i - k]);
      ret = max(ret, v += vset.count(s[i]));
    }
    return ret;
  }
};
```
## Tags

* [Sliding window](/Collections/sliding-window.md#sliding-window)
