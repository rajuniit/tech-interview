# Given an integer array nums sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Example 1:
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]

# Requirement Clarifications

# Q1. Are those numbers sorted? Ans: Yes
# Q2. Can we use extra space? Ans: No
# Q3. Do we need to handle or consider integer overflow? Ans: No
# Q4. What should I return after removing duplicates? Ans: Size of unique element
# Q5. Are there only integer number? Yes
# Q6. What is the length of array would be? Ans: 3 * 10000

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

    # Time complexity: O(n), Space Complexity: O(1)
    def solution1(self, nums: List[int]) -> int:
        if len(nums) == 0: # if list is empty
            return 0
        non_duplicate_index = 0
        next_index = 1
        while next_index < len(nums):
            if nums[non_duplicate_index] != nums[next_index]:
                non_duplicate_index += 1
                nums[non_duplicate_index] = nums[next_index]
            next_index += 1
        return non_duplicate_index + 1 # because array index 0 based


class TestSolution(unittest.TestCase):

    def setUp(self) -> None:
        self.test_cases = [
            {'array': [1,1,2], 'answer': 2},
            {'array': [0,0,1,1,1,2,2,3,3,4], 'answer': 5}
        ]
        self.solution = Solution()

    def test_solution_1(self):
        for test_case in self.test_cases:
            self.assertEqual(self.solution.solution1(test_case['array']), test_case['answer'])
