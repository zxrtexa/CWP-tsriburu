#!/usr/bin/env python3

x = 0
y = 0
while x <= 10:
    print(f"Table de {x}:", end=" ")
    while y <= 10:
        print(y*x , end=" ")
        y+=1
    print(" ")
    y=0
    x+=1