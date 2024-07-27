# Coding: utf-8

# Author: Mingzhe Du (mingzhe@nus.edu.sg)
# Date: 2024 / 07 / 26

import re

few_shot_prompt = """
Example Question and Solution:
        
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]] Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

```python
import json

def spiralOrder(matrix):
    if not matrix or not matrix[0]:
        return []
    rows, cols = len(matrix), len(matrix[0])
    result = []
    x, y = 0, 0
    dx, dy = 1, 0
    for _ in range(rows * cols):
        result.append(matrix[y][x])
        matrix[y][x] = float('inf')
        if not (0 <= x + dx < cols and 0 <= y + dy < rows) or matrix[y + dy][x + dx] == float('inf'):
            dx, dy = -dy, dx
        x += dx
        y += dy
    return result
    
N = int(input())

for _ in range(N):
    input_ = eval(input())
    result = spiralOrder(*input_)
    print(result)
```

Example Question and Solution:

Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

  Example 1:

Input: root = [3,9,20,null,null,15,7] Output: 24 Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:

Input: root = [1] Output: 0

  Constraints:
  
The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000

```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def binaryTree(arr):
    if not arr:
        return None
    N = len(arr)
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue:
        cur = queue.pop(0)
        if i < N:
            if arr[i] is not None:
                cur.left = TreeNode(arr[i])
                queue.append(cur.left)
            i += 1
            if i < N:
                if arr[i] is not None:
                    cur.right = TreeNode(arr[i])
                    queue.append(cur.right)
                i += 1
    return root

def sumOfLeftLeaves(n):
    return (f:=lambda n,q=0:n and f(l:=n.left,1)+f(r:=n.right)+n.val*(l==r==None)*q or 0)(n)

N = int(input())

for _ in range(N):
    input_ = input()
    input_ = input_.replace('null', 'None')
    input_ = eval(input_)
    input_ = [binaryTree(*input_)]
    
    result = sumOfLeftLeaves(*input_)
    print(result)

Example Question and Solution:

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

  Example 1:

Input: digits = [1,2,3] Output: [1,2,4] Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124. Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1] Output: [4,3,2,2] Explanation: The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322. Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9] Output: [1,0] Explanation: The array represents the integer 9. Incrementing by one gives 9 + 1 = 10. Thus, the result should be [1,0].

  Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

```python
import json

def plusOne(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    return [1] + digits

N = int(input())

for _ in range(N):
    input_ = eval(input())
    result = plusOne(*input_)
    print(result)
```

Given the examples coding style, write the solution for the following question. Please ONLY generate the code solution (explicitly import all libraries).
        """
        
def code_match(raw_code):
    pattern = r'```python(.*?)```'
    matches = re.findall(pattern, raw_code, re.DOTALL)
    return matches
    