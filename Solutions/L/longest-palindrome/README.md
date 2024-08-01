# Longest palindrome

[Problem link](https://leetcode.com/problems/longest-palindrome)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-palindrome

class Solution {
 public:
  int longestPalindrome(string s) {
    unordered_map<char, int> cnt;
    for (char c : s) cnt[c]++;
    int best = 0, odd = 0;
    for (auto& c : cnt) {
      if (c.second & 1) odd = c.second--;
      best += c.second;
    }
    if (odd) best++;
    return best;
  }
};
```
## Tags

* [Counting elements in array](/Collections/counting-elements-in-array.md#counting-elements-in-array)
* [Palindrome](/Collections/palindrome.md#palindrome)
