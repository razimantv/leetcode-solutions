# Implement stack using queues

[Problem link](https://leetcode.com/problems/implement-stack-using-queues)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/implement-stack-using-queues

class MyStack {
 public:
  queue<int> q1, q2;

  MyStack() {}

  void push(int x) { q1.push(x); }

  int pop(int p = 1) {
    while (q1.size() > 1) {
      int x = q1.front();
      q1.pop();
      q2.push(x);
    }

    int ret = q1.front();
    q1.pop();
    if (!p) q2.push(ret);

    while (!q2.empty()) {
      int x = q2.front();
      q2.pop();
      q1.push(x);
    }
    return ret;
  }

  int top() { return pop(0); }

  bool empty() { return q1.empty(); }
};

```
## Tags

* [Design data structure](/Collections/design-data-structure.md#design-data-structure) > [Interconversion](/Collections/design-data-structure.md#interconversion)
