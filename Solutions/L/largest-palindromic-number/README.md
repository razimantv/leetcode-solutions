# Largest palindromic number

[Problem link](https://leetcode.com/problems/largest-palindromic-number)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/largest-palindromic-number

class Solution {
 public:
  string largestPalindromic(string num) {
    map<char, int> cnt;
    for (char c : num) ++cnt[c];
    if (cnt.size() == 1 and cnt.count('0')) return "0";

    string ret;
    for (auto mit = cnt.rbegin(); mit != cnt.rend(); ++mit) {
      auto [c, v] = *mit;
      if (ret.size() or c > '0') ret += string(v / 2, c);
    }

    string rev{ret};
    reverse(rev.begin(), rev.end());

    for (auto mit = cnt.rbegin(); mit != cnt.rend(); ++mit) {
      auto [c, v] = *mit;
      if (v & 1) return ret + c + rev;
    }
    return ret + rev;
  }
};
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome)
* [Counting elements in array](/Collections/counting-elements-in-array.md#counting-elements-in-array)
