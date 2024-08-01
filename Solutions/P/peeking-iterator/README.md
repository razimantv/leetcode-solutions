# Peeking iterator

[Problem link](https://leetcode.com/problems/peeking-iterator)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/peeking-iterator

/*
 * Below is the interface for Iterator, which is already defined for you.
 * **DO NOT** modify the interface for Iterator.
 *
 *  class Iterator {
 *		struct Data;
 * 		Data* data;
 *		Iterator(const vector<int>& nums);
 * 		Iterator(const Iterator& iter);
 *
 * 		// Returns the next element in the iteration.
 *		int next();
 *
 *		// Returns true if the iteration has more elements.
 *		bool hasNext() const;
 *	};
 */

class PeekingIterator : public Iterator {
 public:
  bool adv;
  int cache;

  PeekingIterator(const vector<int>& nums)
      : Iterator(nums), adv(false), cache(0) {
    // Initialize any member here.
    // **DO NOT** save a copy of nums and manipulate it directly.
    // You should only use the Iterator interface methods.
  }

  // Returns the next element in the iteration without advancing the iterator.
  int peek() {
    if (adv) return cache;
    adv = true;
    return cache = Iterator::next();
  }

  // hasNext() and next() should behave the same as in the Iterator interface.
  // Override them if needed.
  int next() {
    if (adv) {
      adv = false;
      return cache;
    }
    return Iterator::next();
  }

  bool hasNext() const {
    if (adv)
      return true;
    else
      return Iterator::hasNext();
  }
};
```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
