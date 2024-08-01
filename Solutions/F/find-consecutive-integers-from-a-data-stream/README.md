# Find consecutive integers from a data stream

[Problem link](https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/

class DataStream {
 public:
  int value, k, cnt;
  DataStream(int value, int k) : value(value), k(k), cnt(0) {}

  bool consec(int num) {
    if (num == value)
      ++cnt;
    else
      cnt = 0;
    return cnt >= k;
  }
};
```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
