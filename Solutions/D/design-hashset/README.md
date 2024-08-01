# Design hashset

[Problem link](https://leetcode.com/problems/design-hashset)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/design-hashset

class MyHashSet {
 public:
  /** Initialize your data structure here. */
  constexpr static const int P1 = 101, P2 = 521;
  vector<int> hash[P2];
  MyHashSet() {}

  void add(int key) {
    int k2 = (key * P1) % P2;
    for (int x : hash[k2])
      if (x == key) return;
    hash[k2].push_back(key);
  }

  void remove(int key) {
    int k2 = (key * P1) % P2;
    for (int &x : hash[k2])
      if (x == key) {
        swap(x, hash[k2].back());
        hash[k2].pop_back();
        return;
      }
  }

  /** Returns true if this set contains the specified element */
  bool contains(int key) {
    int k2 = (key * P1) % P2;
    for (int x : hash[k2])
      if (x == key) return true;
    return false;
  }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */
```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
