#!/usr/bin/env python3

original = [2, 8, 9, 48, 8, 22, -12, 2]
new = set()
for i in range(len(original)):
    if original[i] > 5:
        new.add(original[i]+2)
print(original)
print(new)