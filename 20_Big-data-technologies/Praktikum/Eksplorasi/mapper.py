#!/usr/bin/env python3
import sys

def check_palindrome(word):
    return word == word[::-1]

def process_input_mapper(line):
    word = line.strip()
    is_palindrome = check_palindrome(word)
    print(f"{word}\t{is_palindrome}")

if __name__ == "__main__":
    for line in sys.stdin:
        process_input_mapper(line)