# Design a number container system

[Problem link](https://leetcode.com/problems/design-a-number-container-system)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/design-a-number-container-system

class NumberContainers {
 public:
  unordered_map<int, int> fw;
  unordered_map<int, set<int>> bw;
  NumberContainers() {}

  void change(int index, int number) {
    if (fw.count(index)) bw[fw[index]].erase(index);
    fw[index] = number;
    bw[number].insert(index);
  }

  int find(int n) {
    if (bw[n].empty()) return -1;
    return *bw[n].begin();
  }
};

```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue) > [Key update using insert and remove on C++ set](/Collections/priority-queue.md#key-update-using-insert-and-remove-on-c---set)
* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
