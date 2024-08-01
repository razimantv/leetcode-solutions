# First unique character in a string

[Problem link](https://leetcode.com/problems/first-unique-character-in-a-string)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/first-unique-character-in-a-string

class Solution {
 public:
  int firstUniqChar(string s) {
    set<int> uniquepos;
    map<char, int> firstpos;

    for (int i = 0; i < s.size(); i++) {
      char c = s[i];
      if (firstpos.count(c)) {
        if (uniquepos.count(firstpos[c])) uniquepos.erase(firstpos[c]);
      } else {
        firstpos[c] = i;
        uniquepos.insert(i);
      }
    }

    return uniquepos.empty() ? -1 : *uniquepos.begin();
  }
};
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Priority queue](/Collections/priority-queue.md#priority-queue)
