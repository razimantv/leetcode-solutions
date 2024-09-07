# My calendar i

[Problem link](https://leetcode.com/problems/my-calendar-i)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/my-calendar-i

class MyCalendar {
 public:
  map<int, int> events;
  MyCalendar() {}

  bool book(int start, int end) {
    auto mit = events.upper_bound(start);
    if (mit != events.end() and (end > mit->second)) return false;
    events[end] = start;
    return true;
  }
};

```
## Tags

* [Binary search](/Collections/binary-search.md#binary-search) > [C++ set](/Collections/binary-search.md#c---set)
