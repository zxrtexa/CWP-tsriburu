#!/usr/bin/env python3

import sys
lens = len(sys.argv)-1
if (lens) > 1:
    for para in reversed(sys.argv[1:]):
        print(para)
else:
    print("none")