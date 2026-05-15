'''
Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0


The key observation is:

If

```
leftSum == rightSum
```

and

```
totalSum = leftSum + nums[i] + rightSum
```

then:

```
rightSum = totalSum - leftSum - nums[i]
```

So condition becomes:

```
leftSum == totalSum - leftSum - nums[i]
```

Rearrange:

```
2 * leftSum + nums[i] == totalSum
```

---

## Optimal Approach

1. Calculate total sum
2. Traverse array while maintaining left sum
3. Compute right sum mathematically instead of recalculating

```

At index `3`:

* leftSum = 11
* nums[3] = 6

Check:

```
2 * 11 + 6 = 28
```

True ✅

So pivot index = 3

'''