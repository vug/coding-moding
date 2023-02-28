# Trick optimizations

https://leetcode.com/problems/final-value-of-variable-after-performing-operations

## need to store return values to prevent removal by compilation

First of all I've just realized, if I don't store the return value at the call-site, things might get optimized-out by the compiler and my benchmark durations gets small or zero. :-O

With this problem I had to `result = finalValueAfterOperations(inp);`.

One can do `str.compare(otherStr) == 0` to check the operations, but a simpler method I've discovered, that is a specialization for this problem is to check the middle character. for both `++x` and `x++` it's `+`. a similarly for decrement operators it's `-`. So, no need for string comparison, a single character comparison is enough.

## Observations

* Ternary operation is slightly slower than regular if/else

`x += op[1] == '+' ? 1 : -1;` vs `    if (op[1] == '+') ++x; else --x;`