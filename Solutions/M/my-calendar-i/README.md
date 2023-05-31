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

/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar* obj = new MyCalendar();
 * bool param_1 = obj->book(start,end);
 */
```
## Tags

* [Binary search](/README.md#Binary_search) > [C++ set](/README.md#Binary_search-C___set)
