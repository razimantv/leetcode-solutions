# Implement strstr

[Problem link](https://leetcode.com/problems/implement-strstr)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/implement-strstr

class Solution {
 public:
  int strStr(string haystack, string needle) {
    int l = needle.size();
    if (!l) return 0;

    long long p = 354745078340568241, nhash = 0, npow = 1;
    for (char c : needle) {
      nhash = (nhash * 26 + (c - 'a')) % p;
      npow = (npow * 26) % p;
    }

    long long phash = 0;
    for (int i = 0; haystack[i]; ++i) {
      char c = haystack[i];
      phash = (phash * 26 + (c - 'a')) % p;
      if (i >= l)
        phash = (phash + p - (npow * (haystack[i - l] - 'a')) % p) % p;
      if (i >= l - 1 and phash == nhash) return i - l + 1;
    }
    return -1;
  }
};
```
## Tags

* [String](/Collections/string.md#string) > [Search](/Collections/string.md#search) > [Hashing](/Collections/string.md#hashing)
* [Sliding window](/Collections/sliding-window.md#sliding-window) > [String hashing](/Collections/sliding-window.md#string-hashing)
