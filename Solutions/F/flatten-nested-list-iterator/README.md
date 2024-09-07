# Flatten nested list iterator

[Problem link](https://leetcode.com/problems/flatten-nested-list-iterator)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/flatten-nested-list-iterator

class NestedIterator {
 public:
  vector<int> cur;
  int pos = 0;
  void work(vector<NestedInteger> &nestedList) {
    for (auto &n : nestedList) {
      if (n.isInteger())
        cur.push_back(n.getInteger());
      else
        work(n.getList());
    }
  }
  NestedIterator(vector<NestedInteger> &nestedList) { work(nestedList); }

  int next() { return cur[pos++]; }

  bool hasNext() { return pos < cur.size(); }
};

```
## Tags

* [Flattening](/Collections/flattening.md#flattening)
* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
