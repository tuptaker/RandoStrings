#! /usr/bin/env python

import string
import random
import os

def id_generator(size=6, chars=string.ascii_letters + string.digits):
   return ''.join(random.choice(chars) for x in range(size))

if (os.path.exists('./randstr.txt')):        
    os.remove('./randstr.txt')

fileout = open("./randstr.txt", "w")

index = 0

for index in range(0, 1023):
    curr_password = id_generator(12)
    fileout.write(curr_password + '\n')

fileout.close()
