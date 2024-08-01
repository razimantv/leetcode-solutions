# Design browser history

[Problem link](https://leetcode.com/problems/design-browser-history/)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/design-browser-history/

class BrowserHistory {
 public:
  vector<string> history;
  int pos, cap, last;
  BrowserHistory(string homepage)
      : history({homepage}), pos(0), cap(1), last(0) {}

  void visit(string url) {
    if (pos == cap - 1) {
      history.push_back(url);
      ++cap;
      last = ++pos;
    } else {
      history[last = ++pos] = url;
    }
  }

  string back(int steps) {
    pos -= steps;
    if (pos < 0) pos = 0;
    return history[pos];
  }

  string forward(int steps) {
    pos += steps;
    if (pos > last) pos = last;
    return history[pos];
  }
};
```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
