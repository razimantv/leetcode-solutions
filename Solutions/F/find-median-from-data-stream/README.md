# Find median from data stream

[Problem link](https://leetcode.com/problems/find-median-from-data-stream)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-median-from-data-stream

class MedianFinder {
 public:
  /** initialize your data structure here. */
  multiset<int> right;
  multiset<int, greater<int>> left;
  MedianFinder() {}

  void addNum(int num) {
    left.insert(num);
    right.insert(*left.begin());
    left.erase(left.begin());
    if (left.size() < right.size()) {
      left.insert(*right.begin());
      right.erase(right.begin());
    }
  }

  double findMedian() {
    if (left.size() > right.size()) return *left.begin();
    return (*right.begin() + *left.begin()) / 2.;
  }
};

```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue) > [K smallest/largest elements](/Collections/priority-queue.md#k-smallest-largest-elements) > [Transfer between the two](/Collections/priority-queue.md#transfer-between-the-two)
