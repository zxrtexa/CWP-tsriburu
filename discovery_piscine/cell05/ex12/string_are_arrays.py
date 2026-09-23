#!/usr/bin/env python3

import sys
if (len(sys.argv)-1) > 0:
        string = sys.argv[1]
        z_count = string.count('z')
        if z_count == 0:
            print("none")
        else:
            for i in range(z_count):
                print("z",end="")
else:
    print("none")
    