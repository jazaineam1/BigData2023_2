#!/usr/bin/env python3
import sys

def main():
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            print(f"{len(word)}\t1")

if __name__ == "__main__":
    main()
