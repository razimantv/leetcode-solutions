# Maximum frequency stack

[Problem link](https://leetcode.com/problems/maximum-frequency-stack)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/maximum-frequency-stack

class FreqStack {
 public:
  unordered_map<int, int> freq;
  set<tuple<int, int, int>, greater<tuple<int, int, int>>> best;
  int i;

  FreqStack() {}

  void push(int x) { best.insert({++freq[x], ++i, x}); }

  int pop() {
    auto [f, p, v] = *best.begin();
    best.erase(best.begin());
    --freq[v];
    return v;
  }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 */
```
## Tags

* [Priority queue](/Collections/priority-queue.md#priority-queue)
* [Design data structure](/Collections/design-data-structure.md#design-data-structure)
