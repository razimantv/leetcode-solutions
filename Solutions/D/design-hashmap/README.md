# Design hashmap

[Problem link](https://leetcode.com/problems/design-hashmap)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/design-hashmap

class MyHashMap {
 public:
  /** Initialize your data structure here. */
  vector<vector<pair<int, int>>> hashvec;
  MyHashMap() { hashvec = vector<vector<pair<int, int>>>(1024); }

  int hash(int x) { return (x * 313) & 1023; }
  /** value will always be non-negative. */
  void put(int key, int value) {
    int h = hash(key);
    for (auto& [x, y] : hashvec[h]) {
      if (x == key) {
        y = value;
        return;
      }
    }
    hashvec[h].push_back({key, value});
  }

  /** Returns the value to which the specified key is mapped, or -1 if this map
   * contains no mapping for the key */
  int get(int key) {
    int h = hash(key);
    for (auto& [x, y] : hashvec[h]) {
      if (x == key) return y;
    }
    return -1;
  }

  /** Removes the mapping of the specified value key if this map contains a
   * mapping for the key */
  void remove(int key) {
    int h = hash(key);
    for (auto& [x, y] : hashvec[h]) {
      if (x == key) {
        x = hashvec[h].back().first;
        y = hashvec[h].back().second;
        hashvec[h].pop_back();
      }
    }
  }
};

```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap)
* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
