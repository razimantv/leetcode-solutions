# The dining philosophers

[Problem link](https://leetcode.com/problems/the-dining-philosophers)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/the-dining-philosophers

class DiningPhilosophers {
 public:
  static mutex m;
  DiningPhilosophers() {}

  void wantsToEat(int philosopher, function<void()> pickLeftFork,
                  function<void()> pickRightFork, function<void()> eat,
                  function<void()> putLeftFork, function<void()> putRightFork) {
    lock_guard<mutex> lock(m);
    pickLeftFork();
    pickRightFork();
    eat();
    putLeftFork();
    putRightFork();
  }
};

mutex DiningPhilosophers::m;
```