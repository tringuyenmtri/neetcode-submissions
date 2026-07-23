#!/bin/python3

import math
import os
import random
import re
import sys

#
# Source Question:
# https://www.hackerrank.com/contests/software-engineer-prep-kit/challenges/validate-properly-nested-brackets/problem
# https://leetcode.com/problems/valid-parentheses/description/
# https://neetcode.io/problems/validate-parentheses/question
#

# Problem Statement:
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
#   1. Every open bracket is closed by the same type of close bracket.
#   2. Open brackets are closed in the correct order.
#   3. Every close bracket has a corresponding open bracket of the same type.
#
# Return true if s is a valid string, and false otherwise.

# Solution Pseudo-Code:
# Use a stack to keep track of bracket characters.
# Push opening characters onto the stack.
# If a closing character is seen, then pop character off the stack and match it with the current character
# as a closing character.
#
# 1. Iterate through string parameter one character at a time
#   1. If the current character is an opening character, then push the character onto the stack
#   2. If the current character is a closing character, then pop a character from the stack.
#   3. If the pop-ed character is a corresponding opening character, then move on to next character in string method parameter.
#   4. If the pop-ed character is NOT a corresponding opening character, then return False.
# 2. If string method parameter is been throughly processed to the end, then return True.

class Solution:
    def isValid(self, s: str) -> bool:
        string_stack: list[str] = []
        for char in s:
            if (char == '(') or (char == '{') or (char == '['):
                string_stack.append(char)
            elif (char == ')') or (char == '}') or (char == ']'):
                if not string_stack:
                    return False
                if (char == ')' and string_stack[-1] == '(') or (char == '}' and string_stack[-1] == '{') or (char == ']' and string_stack[-1] == '['):
                    string_stack.pop()
                else:
                    return False


        if not string_stack:
            return True
        return False
