# Seat reservation manager

[Problem link](https://leetcode.com/problems/seat-reservation-manager)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/seat-reservation-manager

class SeatManager {
 public:
  set<int> s;
  SeatManager(int n) {
    for (int i = 1; i <= n; ++i) s.insert(i);
  }

  int reserve() {
    int ret = *s.begin();
    s.erase(ret);
    return ret;
  }

  void unreserve(int seatNumber) { s.insert(seatNumber); }
};
```