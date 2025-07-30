'''
**Problem Description**

In this problem, we are given an integer length which refers to the length of an array initially filled with zeros.
We are also given an array of update operations called updates.
Each update operation is described as a tuple or list with three integers: [startIdx, endIdx, inc].
For each update operation, we are supposed to add the value inc to each element of the array starting at/
 index startIdx up to and including the index endIdx.

The goal is to apply all the update operations to the array and then return the modified array.

For instance, if length = 5 and an update action specifies [1, 3, 2],
then after this update, the array will have 2 added to its 1st, 2nd, and 3rd positions (keeping zero-based indexing in mind),
 resulting in the array [0, 2, 2, 2, 0] after this single operation.

After applying all updates, we need to return the final state of the array.
'''

'''
Solution:
1. Initialize an array of given length with all zeros.

2. For each update [start, end, inc], do arr[start] += inc and arr[end + 1] -= inc (if end + 1 < length).

3. Take the prefix sum of the array to get the final updated array.
'''
import logging
class RangeAddition():
    def rng_add(self,arr_ln:int, update_dsc_ary:list[list[int]])->list[int]:
        try:
            res_ary = [0]*arr_ln
            for st_i,en_i,inc in update_dsc_ary:
                res_ary[st_i] += inc
                if en_i+1<arr_ln:
                    res_ary[en_i+1] -= inc
            for i in range(arr_ln):
                if i != 0:
                    res_ary[i] += res_ary[i-1]
            return res_ary
        except Exception as e:
            logging.error(f"ERROR >> {e}")
            return []
sol = RangeAddition()
aryLen = 5
update_data = [[1, 3, 2],[2,4,3],[0,2,-2]]
res = sol.rng_add(aryLen,update_data)
print(res)
