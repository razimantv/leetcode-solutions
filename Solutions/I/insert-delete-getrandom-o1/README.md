# Insert delete getrandom o1

[Problem link](https://leetcode.com/problems/insert-delete-getrandom-o1)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/insert-delete-getrandom-o1

class RandomizedSet {
 public:
  unordered_map<int, int> Pos;
  vector<int> Val;

  /** Initialize your data structure here. */
  RandomizedSet() {
    Pos.clear();
    Val.clear();
  }

  /** Inserts a value to the set. Returns true if the set did not already
   * contain the specified element. */
  bool insert(int val) {
    if (Pos[val]) return false;
    Val.push_back(val);
    Pos[val] = Val.size();
    return true;
  }

  /** Removes a value from the set. Returns true if the set contained the
   * specified element. */
  bool remove(int val) {
    int p = Pos[val];
    if (p == 0) return false;
    int v = Val.back();
    Pos[v] = p;
    Pos[val] = 0;
    Val[p - 1] = v;
    Val.pop_back();
    return true;
  }

  /** Get a random element from the set. */
  int getRandom() { return Val[rand() % Val.size()]; }
};

```
## Tags

* [Hashmap](/Collections/hashmap.md#hashmap) > [Forward and backward](/Collections/hashmap.md#forward-and-backward)
* [Mathematics](/Collections/mathematics.md#mathematics) > [Probability](/Collections/mathematics.md#probability)
* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
