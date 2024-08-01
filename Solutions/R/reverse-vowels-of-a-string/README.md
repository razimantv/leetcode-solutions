# Reverse vowels of a string

[Problem link](https://leetcode.com/problems/reverse-vowels-of-a-string/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution {
 public:
  string reverseVowels(string s) {
    unordered_set<char> vowels{'a', 'e', 'i', 'o', 'u'};
    for (int i = 0, n = s.size(), j = n - 1; i < j;) {
      if (!vowels.count(tolower(s[i])))
        ++i;
      else if (!vowels.count(tolower(s[j])))
        --j;
      else
        swap(s[i++], s[j--]);
    }
    return s;
  }
};
```
## Tags

* [Array scanning](/Collections/array-scanning.md#array-scanning) > [In-place modification](/Collections/array-scanning.md#in-place-modification)
* [Two pointers](/Collections/two-pointers.md#two-pointers)
