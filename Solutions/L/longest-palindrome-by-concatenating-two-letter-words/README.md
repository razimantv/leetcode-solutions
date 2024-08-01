# Longest palindrome by concatenating two letter words

[Problem link](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution {
 public:
  int longestPalindrome(vector<string>& words) {
    unordered_multiset<string> seen;
    int ret{};
    for (string s : words) {
      string ss = s;
      swap(ss[0], ss[1]);
      if (seen.count(ss)) {
        ret += 4;
        seen.erase(seen.find(ss));
      } else {
        seen.insert(s);
      }
    }

    for (string s : seen) {
      if (s[0] == s[1]) return ret + 2;
    }
    return ret;
  }
};
```
## Tags

* [Palindrome](/Collections/palindrome.md#palindrome)
* [Hashmap](/Collections/hashmap.md#hashmap)
