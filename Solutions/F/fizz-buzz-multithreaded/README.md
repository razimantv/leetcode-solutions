# Fizz buzz multithreaded

[Problem link](https://leetcode.com/problems/fizz-buzz-multithreaded)

## Solutions


### Solution.cpp
```cpp
// https://leetcode.com/problems/fizz-buzz-multithreaded

class FizzBuzz {
 private:
  int n;
  mutex m;
  condition_variable cv;
  int status;

 public:
  FizzBuzz(int n) {
    this->n = n;
    status = 0;
    cv.notify_all();
  }

  // printFizz() outputs "fizz".
  void fizz(function<void()> printFizz) {
    for (int i = 1; i <= n; ++i) {
      {
        unique_lock<mutex> lk(m);
        cv.wait(lk, [&]() { return (status & 1) == 0; });
        if (i % 3 == 0 and i % 5 != 0) printFizz();
        status |= 1;
        if (status == 15) status = 0;
      }
      cv.notify_all();
    }
  }

  // printBuzz() outputs "buzz".
  void buzz(function<void()> printBuzz) {
    for (int i = 1; i <= n; ++i) {
      {
        unique_lock<mutex> lk(m);
        cv.wait(lk, [&]() { return (status & 2) == 0; });
        if (i % 3 != 0 and i % 5 == 0) printBuzz();
        status |= 2;
        if (status == 15) status = 0;
      }
      cv.notify_all();
    }
  }

  // printFizzBuzz() outputs "fizzbuzz".
  void fizzbuzz(function<void()> printFizzBuzz) {
    for (int i = 1; i <= n; ++i) {
      {
        unique_lock<mutex> lk(m);
        cv.wait(lk, [&]() { return (status & 4) == 0; });
        if (i % 3 == 0 and i % 5 == 0) printFizzBuzz();
        status |= 4;
        if (status == 15) status = 0;
      }
      cv.notify_all();
    }
  }

  // printNumber(x) outputs "x", where x is an integer.
  void number(function<void(int)> printNumber) {
    for (int i = 1; i <= n; ++i) {
      {
        unique_lock<mutex> lk(m);
        cv.wait(lk, [&]() { return (status & 8) == 0; });
        if (i % 3 != 0 and i % 5 != 0) printNumber(i);
        status |= 8;
        if (status == 15) status = 0;
      }
      cv.notify_all();
    }
  }
};
```
## Tags

* [Concurrency](/Collections/concurrency.md#concurrency)
