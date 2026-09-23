#!/usr/bin/env python3

import sys
if (len(sys.argv)-1) > 0:
    keyword = sys.argv[1]
    input_word = input("What was the parameter? ")
    if keyword == input_word:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")