class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Problem Statement:
        # You are given two strings needle and haystack,
        # return the index of the first occurrence of needle in haystack,
        # or -1 if needle is not part of haystack.
        #
        # Pseudo-Code Solution:
        # 1. Starting at the 1st character of haystack, iterate through each character until the last character of haystack.
        #    1. At the current index, extract the next substring of length equal to the length of needle.
        #    2. If the extracted substring matches needle, return the current index.
        #    3. Otherwise, continue iterating.
        # 2. Return -1
        for index, char in enumerate(haystack):
            endingIndex: int = index + len(needle)
            if endingIndex > len(haystack):
                return -1
            if (haystack[index:endingIndex] == needle):
                return index
        return -1
