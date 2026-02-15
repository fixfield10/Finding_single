Finding the Happiest Single
Problem

Given a list of numbers where every element appears exactly twice except one, find the element that appears only once.

Example:
Input: [1, 1, 2, 2, 3]
Output: [3]

Approach

The function uses a dictionary to store the frequency of each number in the list.
It then filters out the number whose count is equal to 1 using list comprehension.
That number is returned as the single (non-repeating) element.

Concepts Used

Dictionary (Hash Map)

Frequency counting

List comprehension

This solution focuses on clarity and uses basic data structure concepts to solve the problem.
