#!/usr/bin/env python3
"""palindrome - Check strings and find palindromes."""
import sys, re

def is_palindrome(s):
    clean = re.sub(r"[^a-z0-9]", "", s.lower())
    return clean == clean[::-1]

def longest_palindrome(s):
    clean = s.lower()
    best = ""
    for i in range(len(clean)):
        for j in range(i+1, len(clean)+1):
            sub = clean[i:j]
            if sub == sub[::-1] and len(sub) > len(best): best = sub
    return best

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: palindrome <check|find> <text>"); sys.exit(1)
    cmd = sys.argv[1]
    text = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
    if cmd == "check":
        print(f"\"{text}\" is{'' if is_palindrome(text) else ' NOT'} a palindrome")
    elif cmd == "find":
        lp = longest_palindrome(text)
        print(f"Longest palindrome: \"{lp}\" (len {len(lp)})")
    else:
        print(f"\"{cmd}\" is{'' if is_palindrome(cmd) else ' NOT'} a palindrome")
