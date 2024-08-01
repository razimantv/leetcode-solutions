# Longest uploaded prefix

[Problem link](https://leetcode.com/problems/longest-uploaded-prefix/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/longest-uploaded-prefix/

class LUPrefix {
 public:
  unordered_set<int> seen;
  int good;
  LUPrefix(int n) : good(0) {}

  void upload(int video) {
    seen.insert(video);
    if (video == 1 or good == video - 1) {
      while (seen.count(video)) good = video++;
    }
  }

  int longest() { return good; }
};

/**
 * Your LUPrefix object will be instantiated and called as such:
 * LUPrefix* obj = new LUPrefix(n);
 * obj->upload(video);
 * int param_2 = obj->longest();
 */
```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
