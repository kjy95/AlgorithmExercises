#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
def exact(mon,minous):
    if mon-minous<0:
        sys.stdout.write(mon)
        sys.exit(1)
        return mon
    else:
        print(mon-minous)

        return mon-minous
if __name__ == '__main__':
    split = sys.stdin.readline().strip().split(' ')
    money = 20000
    for token in split:
        distance = int(token)
        if distance < 4 or distance > 178:
            sys.stdout.write(str(int(money)))
            sys.exit(1)
        
        elif distance<=40:
            money= exact(money,720) 
            print(money)
        else :
            money= exact(money,720) 
            distance -= 40
            money = exact(money,80*(int(distance/8)))
            print(money)
            

    sys.stdout.write(str(int(money)))
        # @todo Write your code here.
    # @todo Write your code here.
    print(int(71/8))