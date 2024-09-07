# Kth largest element in a stream

[Problem link](https://leetcode.com/problems/kth-largest-element-in-a-stream)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/kth-largest-element-in-a-stream

class KthLargest {
 public:
  multiset<int> heap;
  int k;
  KthLargest(int k, vector<int>& nums) : k(k) {
    for (int x : nums) add(x);
  }

  int add(int val) {
    heap.insert(val);
    if (heap.size() > k) heap.erase(heap.begin());
    return *heap.begin();
  }
};

```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue) > [K smallest/largest elements](/Collections/priority-queue.md#k-smallest-largest-elements)
