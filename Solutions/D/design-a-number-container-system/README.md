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

/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers* obj = new NumberContainers();
 * obj->change(index,number);
 * int param_2 = obj->find(number);
 */
```
## Tags

* [Priority queue](/README.md#Priority_queue) > [Key update using insert and remove on C++ set](/README.md#Priority_queue-Key_update_using_insert_and_remove_on_C___set)
* [Design data structure](/README.md#Design_data_structure)
