#!/usr/bin/python3
"""
Test script for number_of_subscribers function.
"""
import sys
from 0-subs import number_of_subscribers

def main():
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print(f"Number of subscribers for subreddit '{subreddit}': {number_of_subscribers(subreddit)}")

if __name__ == '__main__':
    main()
