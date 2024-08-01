# Frequency tracker

[Problem link](https://leetcode.com/problems/frequency-tracker/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/frequency-tracker/

class FrequencyTracker {
 public:
  unordered_map<int, int> cnt, fcnt;
  FrequencyTracker() {}

  void add(int number) {
    if (cnt[number]) --fcnt[cnt[number]];
    ++fcnt[++cnt[number]];
  }

  void deleteOne(int number) {
    if (cnt[number]) {
      --fcnt[cnt[number]];
      if (--cnt[number]) ++fcnt[cnt[number]];
    }
  }

  bool hasFrequency(int frequency) { return fcnt[frequency]; }
};
```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
* [Hashmap](/Collections/hashmap.md#hashmap) > [Forward and backward](/Collections/hashmap.md#forward-and-backward)
