#!/usr/bin/env python3
"""Palindrome checker and longest palindrome finder."""
import sys, re
def is_palindrome(s):
    s = re.sub(r'[^a-z0-9]', '', s.lower())
    return s == s[::-1]
def longest_palindrome(s):
    s = s.lower(); best = ""
    for i in range(len(s)):
        for d in [0, 1]:
            lo, hi = i, i + d
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1; hi += 1
            if hi - lo - 1 > len(best): best = s[lo+1:hi]
    return best
if __name__ == "__main__":
    if len(sys.argv) < 2:
        tests = ["racecar", "A man a plan a canal Panama", "hello", "Was it a car or a cat I saw"]
        for t in tests: print(f"  '{t}': {is_palindrome(t)}")
    else:
        text = " ".join(sys.argv[1:])
        print(f"Palindrome: {is_palindrome(text)}")
        lp = longest_palindrome(text)
        if lp: print(f"Longest palindromic substring: '{lp}'")
