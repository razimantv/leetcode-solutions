# Sort vowels in a string

[Problem link](https://leetcode.com/problems/sort-vowels-in-a-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/sort-vowels-in-a-string/

class Solution {
 public:
  string sortVowels(string s) {
    string vowels;
    unordered_set<char> good;
    for (char c : "aeiou") good.insert(c), good.insert(toupper(c));
    for (char c : s)
      if (good.count(c)) vowels.push_back(c);
    sort(vowels.begin(), vowels.end());
    for (int i = 0, j = 0; s[i]; ++i)
      if (good.count(s[i])) s[i] = vowels[j++];
    return s;
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
