#!/usr/bin/env python3
"""Palindrome checker and longest palindrome finder."""
import sys, re

def is_palindrome(s):
    clean = re.sub(r'[^a-z0-9]', '', s.lower())
    return clean == clean[::-1]

def longest_palindrome(s):
    clean = re.sub(r'[^a-z0-9]', '', s.lower())
    best = ''
    for i in range(len(clean)):
        for j in range(i+1, len(clean)+1):
            sub = clean[i:j]
            if sub == sub[::-1] and len(sub) > len(best):
                best = sub
    return best

if __name__ == '__main__':
    if len(sys.argv) < 2: print("Usage: palindrome.py <check|longest> <text>"); sys.exit(1)
    cmd = sys.argv[1]
    text = ' '.join(sys.argv[2:])
    if cmd == 'check':
        result = is_palindrome(text)
        print(f"'{text}' {'is' if result else 'is NOT'} a palindrome")
    elif cmd == 'longest':
        print(f"Longest palindrome: {longest_palindrome(text)}")
    else:
        result = is_palindrome(' '.join(sys.argv[1:]))
        print(f"{'✓ Palindrome' if result else '✗ Not a palindrome'}")
