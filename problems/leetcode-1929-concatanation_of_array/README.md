# Concatanations, copies, filling, vector allocation...

## Intro

From C++ perspective, this is about implementing concatanation operation. Other languages come with concatanation as part of the language. For example, in Python the anser is `return nums + nums` or something. :-O

I mean, it's specifically a concat of a vector by itself and this specialization provides an advantage to pure loop based solution. But if we think about further generalizations (concat of two different vectors, or concat of the same vector N times) then that solution might lose it's advantage.

Here are some solutions

## compilation

Don't forget to optimize for more realistic benchmarking

```
g++ -std=c++20 -O3 main.cpp -o solution
```

Variations on duration of each version among various runs were high. But the relative durations of each version per run was consistent most of the time.

```
106 106 160 105 213 173 150 154 106 161 178
```

## For loop and assignment with pre-allocation

```cpp
std::vector<int> getConcatenation1(std::vector<int> &nums) {
  const size_t n = nums.size();
  std::vector<int> ans(2 * n);
  for (size_t i = 0; i < n; ++i)
    ans[i] = ans[i + n] = nums[i];
  return ans;
}
```

* Allocates the vector at constructor.
* Basic for loop, with double assignment
* Can be generalized to `m` concats via

```cpp
  for (size_t i = 0; i < n; ++i)
    for (int k = 0; k < m; ++k)
      ans[i + k * n] = nums[i];
```

* A slight variation is to construct empty vector and resize it later. I think both requires type to be default constructable and probably do the same

```cpp
  std::vector<int> ans;
  ans.resize(2 * n);
```

## Copy at construction

Tried some variations of

```cpp
  const size_t n = nums.size();
  std::vector<int> ans(nums);
  ans.reserve(2 * n);
  for (int x : nums)
    ans.push_back(x);
```

* Copying first `num` at constructor, then doing push back (or other copying methods)
* These weren't as performant as others

## vector::insert

```cpp
  ans.reserve(2 * n);
  ans.insert(ans.end(), nums.begin(), nums.end());
  ans.insert(ans.end(), nums.begin(), nums.end());
```

* empty construct
* `reserve` (not `resize`)
* use `insert` to copy `nums` into `ans`

This uses vector specific `insert` method for copying, which usually is as performant as for loop

If the the problem won't be generalized to other types of containers I'd choose this as my solution, because it is very easy to generalize N copies of same vector or M different vectors

Note that one copy at construction 

```cpp
  std::vector<int> ans(nums);
  ans.reserve(2 * n);
  ans.insert(ans.end(), nums.begin(), nums.end());
```

## std::copy

This is less performant then `std::vector::insert`, I guess, because it cannot exploit vector's properties.

```cpp
  std::vector<int> ans;
  ans.reserve(2 * n);
  std::copy(nums.begin(), nums.end(), std::back_inserter(ans));
  std::copy(nums.begin(), nums.end(), std::back_inserter(ans));
```

Same structure as `insert` version. parameter meaning and order are different though. Uses `back_inserter` instead of `.end()`. 

* refresher on `back_inserter` [c\+\+ \- Why use std::back\_inserter instead of end\(\) during std::copy? \- Stack Overflow](https://stackoverflow.com/questions/54297642/why-use-stdback-inserter-instead-of-end-during-stdcopy) 
  * It's an algorithm thing. It'll make the vector grow if it hits the capacity.
  * Using `ans.end()` would be Undefined Behavior (UB)

## Vector copy summary

* copy at constructor
* resize and for loop assignment
* reserve and push back
* reserve and insert
* reserve and copy

Reserve probably is more needed when arbitrary number of concats happen. 

## Generalizations

* concat same vector not 2 but N times
* different value types for the Vector
  * I think the results might differ depending on whether the type is a primitive or an class with constructor.
  * generic, templated solution
* concat N different vectors
  * can be a container of N vectors or variadic parameters

## References

* [std::iota \- cppreference\.com](https://en.cppreference.com/w/cpp/algorithm/iota) to fill a container with consecutive values. `[5, 6, 7, 8...]` 
  * used it to generate input data
```cpp
  std::vector<int> inp(10'000'000);
  std::iota(inp.begin(), inp.end(), 0);
```
  * Also has a ranges version in c++23: `std::ranges::iota(inp, 0);`. See [std::ranges::iota \- cppreference\.com](https://en.cppreference.com/w/cpp/algorithm/ranges/iota)
  * and a view version in c++20 [std::ranges::views::iota, std::ranges::iota\_view \- cppreference\.com](https://en.cppreference.com/w/cpp/ranges/iota_view)
* [std::vector \- cppreference\.com](https://en.cppreference.com/w/cpp/container/vector)
  * Constructor [std::vector<T,Allocator>::vector \- cppreference\.com](https://en.cppreference.com/w/cpp/container/vector/vector)
  * [std::vector<T,Allocator>::insert \- cppreference\.com](https://en.cppreference.com/w/cpp/container/vector/insert) Very good to copy a container into another
* [std::copy, std::copy\_if \- cppreference\.com](https://en.cppreference.com/w/cpp/algorithm/copy)
* .
* [c\+\+ \- Do iota, generate, and a hand rolled loop all perform the same? \- Stack Overflow](https://stackoverflow.com/questions/25475677/do-iota-generate-and-a-hand-rolled-loop-all-perform-the-same)
* [c\+\+ \- Efficiency when populating a vector \- Stack Overflow](https://stackoverflow.com/questions/9121454/efficiency-when-populating-a-vector)