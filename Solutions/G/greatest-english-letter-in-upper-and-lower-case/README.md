# Greatest english letter in upper and lower case

[Problem link](https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case

class Solution {
 public:
  string greatestLetter(string s) {
    map<char, int> m;
    for (char c : s)
      if (isupper(c))
        m[c] |= 1;
      else
        m[toupper(c)] |= 2;
    for (auto mit = m.rbegin(); mit != m.rend(); ++mit)
      if (mit->second == 3) return string(1, mit->first);
    return "";
  }
};
```
## Tags

* [Simple implementation](/Collections/simple-implementation.md#simple-implementation)
* [Hashmap](/Collections/hashmap.md#hashmap)
