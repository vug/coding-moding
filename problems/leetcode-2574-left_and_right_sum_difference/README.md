# Fewer loops and less memory by being clever

https://leetcode.com/problems/left-and-right-sum-differences/

tags: array, cumulative continuous sum

I first thought there might be some clever mathematical relation that'll give the solution in one loop with no memory. But apparently that's not the case. Because of my theoretical physics background I tend to believe that there is such a solution and go for it. Shouldn't do that in a real interview.

```
nums      10  4   8  3
leftSums   0 10  14 22
rigthSums 15 11   3  0

leftSum[i] = sum_{i=-1}{j-1} nums[i]
rightSum[i] = sum_{i=j+1}{N} nums[i]
```

If it was an addition, sure something would showed up, but it's subtraction.

Then I did the basic, loop-based solution. Stored left and right sums in their own vectors.

```cpp
  std::vector<int> leftSum(nums.size());
  std::vector<int> rightSum(nums.size());
  std::vector<int> answer(nums.size());
  leftSum[0] = 0;
  rightSum[nums.size() - 1] = 0;
  for (int i = 1; i < nums.size(); ++i)
    leftSum[i] = leftSum[i - 1] + nums[i - 1];
  for (int i = nums.size() - 2; i > -1; --i)
    rightSum[i] = rightSum[i + 1] + nums[i + 1];
  for (int i = 0; i < nums.size(); ++i)
    answer[i] = abs(leftSum[i] - rightSum[i]);
  return answer;
```

The issue with this solution, other than wasting memory and multiple loops, is that, the indices are complex. The rule for nums[-1] == nums[N] == 0, made me use these indices. But in a live interview high chance that I'll make a off-by-one mistake pursuing this path.

This should be the brute force solution that is told verbally. "I can use three vectors of size N. Loop left-to-right fill leftSum. Loop right-to-left fill rightSum. Then loop any direction again and calculate answer. But probably this wastes memory, and maybe loops. Let me think of something better first."

The trick of this problem is the relation between total and left, right values at an index. If we go from left-to-right we can calculate the leftSum value per index on the fly, by just calculating cumulative sum. (similar is true for going right-to-left and rightSum). So, that's a strong indicator that, we can get rid off one loop, if we have can deduce the rightSum from total.

Thinking of benefits of having total (with the cost of one O(N) loop, stored in O(1)) should be very natural given that this is a cumulative sum problem. "Can I calculate rightSum and the answer per index in the same loop?" -> yes, if I've the total.

## considerations, generalizations

* this type of problems probably won't generalize easily. First, it's too made-up, not real-life use.
* Other types that can be added.
* Consider overflows. Mentioning this might be important and a solution could be to have constraints on maximum number and size of input or using a BigInteger type.
* Maybe we can push for a 2D case of cumulative sums. In a 2D grid sum of all number in the rectangle from this index to four corners. And of course from there to N-Dim case.