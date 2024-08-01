# Flatten nested list iterator

[Problem link](https://leetcode.com/problems/flatten-nested-list-iterator)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/flatten-nested-list-iterator

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than
 * a nested list. bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a
 * single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a
 * nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */

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

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
```
## Tags

* [Flattening](/Collections/flattening.md#flattening)
* [Suboptimal solution](/Collections/suboptimal-solution.md#suboptimal-solution)
