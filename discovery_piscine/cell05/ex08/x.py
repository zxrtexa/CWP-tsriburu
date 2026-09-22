#!/usr/bin/env python3

import sys
if (len(sys.argv)-1) > 1:
    while (len(sys.argv)-1) != 0:
        print(sys.argv.pop())
else:
    print("none")