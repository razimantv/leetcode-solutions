# Design parking system

[Problem link](https://leetcode.com/problems/design-parking-system/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/design-parking-system/

// ChatGPT solution
class ParkingSystem {
 private:
  int slots[4];

 public:
  ParkingSystem(int big, int medium, int small) {
    slots[1] = big;
    slots[2] = medium;
    slots[3] = small;
  }

  bool addCar(int carType) {
    if (slots[carType] > 0) {
      slots[carType]--;
      return true;
    } else {
      return false;
    }
  }
};
```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
* [ChatGPT](/Collections/chatgpt.md#chatgpt)
