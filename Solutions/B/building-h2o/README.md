# Building h2o

[Problem link](https://leetcode.com/problems/building-h2o)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/building-h2o

class H2O {
  static int O, H;
  static condition_variable cv;
  static mutex m;

 public:
  H2O() { cv.notify_one(); }

  void hydrogen(function<void()> releaseHydrogen) {
    {
      unique_lock<mutex> lk(m);
      cv.wait(lk, []() { return H < 2; });

      ++H;
      // releaseHydrogen() outputs "H". Do not change or remove this line.
      releaseHydrogen();

      if (O == 1 and H == 2) O = H = 0;
    }
    cv.notify_one();
  }

  void oxygen(function<void()> releaseOxygen) {
    {
      unique_lock<mutex> lk(m);
      cv.wait(lk, []() { return O < 1; });

      ++O;
      // releaseOxygen() outputs "O". Do not change or remove this line.
      releaseOxygen();

      if (O == 1 and H == 2) O = H = 0;
    }
    cv.notify_one();
  }
};

int H2O::O = 0;
int H2O::H = 0;
condition_variable H2O::cv;
mutex H2O::m;
```
## Tags

* [Concurrency](/Collections/concurrency.md#concurrency)
