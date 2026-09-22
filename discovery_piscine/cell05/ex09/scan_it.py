#!/usr/bin/env python3

import sys
if (len(sys.argv)-1) > 1:
    keyword = sys.argv[1]
    string = sys.argv[2]
    result = (keyword, string)
    print(len(result))
else:
    print("none")