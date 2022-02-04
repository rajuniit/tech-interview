# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Requirement Clarifications

# Q1. Are those numbers sorted?
# Q2. Are there any duplicate numbers?
# Q3. Can we use the same number twice?
# Q4. Do we need to handle or consider integer overflow?
# Q5. What should I return if the answer is not available?
# Q6. What should I return if there are multiple answers?

# STEP WE NEED TO FOLLOW
# Step 01: REQUIREMENT CLARIFICATION WITH INTERVIEWER
# Step 02: DRY RUN WITH AN EXAMPLE TEST CASE
# Step 03: CONCEPTUALIZE THE SOLUTION
# Step 04: SOLUTION 1....SOLUTION N
# Step 05: IMPLEMENTATION OF MOST OPTIMIZED SOLUTION
# Step 06: TEST DRY RUN TO VERIFY SOLUTION
from typing import List
import unittest


class Solution:

    # Time complexity: O(n2), Space Complexity: O(1)
    def solution1(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return nums
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

    # Time complexity: O(n), Space complexity: O(n)
    def solution2(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return []
        dic = {}
        for index, value in enumerate(nums):
            delta = target - value
            if delta in dic:
                return [dic[delta], index]
            dic[value] = index
        return []



class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.test_cases = [
            {'array': [3,4,5,2,6], 'target': 7, 'answer': [0,1]},
            {'array': [2,7,11,15], 'target': 26, 'answer': [2,3]}
        ]
        self.solution = Solution()

    def test_solution_1(self):
        for test_case in self.test_cases:
            self.assertEqual(self.solution.solution1(test_case['array'], test_case['target']), test_case['answer'])

    def test_solution_2(self):
        for test_case in self.test_cases:
            self.assertEqual(self.solution.solution2(test_case['array'], test_case['target']), test_case['answer'])
