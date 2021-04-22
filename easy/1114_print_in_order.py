"""
Suppose we have a class:

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
The same instance of Foo will be passed to three different threads.
Thread A will call first(), thread B will call second(), and thread C will call third().

Design a mechanism and modify the program to ensure that second() is executed after first(), and third()
is executed after second().

Note:
We do not know how the threads will be scheduled in the operating system,
even though the numbers in the input seem to imply the ordering.
The input format you see is mainly to ensure our tests' comprehensiveness.

Example 1:
Input: nums = [1,2,3]
Output: "firstsecondthird"
Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(),
thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.

Example 2:
Input: nums = [1,3,2]
Output: "firstsecondthird"
Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second().
"firstsecondthird" is the correct output.
"""

import threading
from typing import Callable


class Foo:
    """
    Runtime: 40 ms, faster than 65.50% of Python3
    Memory Usage: 14.6 MB, less than 90.08% of Python3
    """

    def __init__(self):
        self.first_job_lock = threading.Lock()
        self.second_job_lock = threading.Lock()
        self.first_job_lock.acquire()
        self.second_job_lock.acquire()

    def first(self, printFirst: Callable[[], None]) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        # release the lock so other thread waiting for it can start
        self.first_job_lock.release()

    def second(self, printSecond: Callable[[], None]) -> None:
        with self.first_job_lock:  # wait here until lock is released in first func
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.second_job_lock.release()

    def third(self, printThird: Callable[[], None]) -> None:
        with self.second_job_lock:
            # printThird() outputs "third". Do not change or remove this line.
            printThird()
