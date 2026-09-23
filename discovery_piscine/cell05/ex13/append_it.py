#!/usr/bin/env python3

import sys
found = False
if len(sys.argv)-1 > 0:
    for i in range(1, len(sys.argv)):
        if not sys.argv[i].endswith("ism"):
            print(f"{sys.argv[i]}ism")
            found = True
if not found:
    print("none")