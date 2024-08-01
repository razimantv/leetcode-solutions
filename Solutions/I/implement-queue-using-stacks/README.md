# Implement queue using stacks

[Problem link](https://leetcode.com/problems/implement-queue-using-stacks)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/implement-queue-using-stacks

class MyQueue {
 public:
  stack<int> s1, s2;
  MyQueue() {}

  void push(int x) { s1.push(x); }

  void fix() {
    if (s2.empty()) {
      while (!s1.empty()) {
        int x = s1.top();
        s1.pop();
        s2.push(x);
      }
    }
  }

  int pop() {
    fix();
    int x = s2.top();
    s2.pop();
    return x;
  }

  int peek() {
    fix();
    int x = s2.top();
    return x;
  }

  bool empty() { return s1.empty() and s2.empty(); }
};
```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure) > [Interconversion](/Collections/design-data-structure.md#interconversion)
