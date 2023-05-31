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

* [Design data structure](/README.md#Design_data_structure)
* [Hashmap](/README.md#Hashmap) > [Forward and backward](/README.md#Hashmap-Forward_and_backward)
