#!/usr/bin/env python3
"""palindrome - Palindrome utilities."""
import sys,argparse,json,re
def is_palindrome(s):
    clean=re.sub(r"[^a-zA-Z0-9]","",s.lower())
    return clean==clean[::-1]
def longest_palindrome(s):
    best=""
    for i in range(len(s)):
        for l in [0,1]:
            lo,hi=i,i+l
            while lo>=0 and hi<len(s) and s[lo]==s[hi]:lo-=1;hi+=1
            if hi-lo-1>len(best):best=s[lo+1:hi]
    return best
def main():
    p=argparse.ArgumentParser(description="Palindrome tool")
    sub=p.add_subparsers(dest="cmd")
    c=sub.add_parser("check");c.add_argument("text")
    l=sub.add_parser("longest");l.add_argument("text")
    args=p.parse_args()
    if args.cmd=="check":print(json.dumps({"text":args.text,"is_palindrome":is_palindrome(args.text)}))
    elif args.cmd=="longest":
        lp=longest_palindrome(args.text)
        print(json.dumps({"text":args.text,"longest":lp,"length":len(lp)}))
    else:p.print_help()
if __name__=="__main__":main()
