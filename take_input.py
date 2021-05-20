# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 15:03:51 2020

@author: kelbla
"""


import sys

import datetime
import os.path

#daily questions

guess1 = input("Mood scr (0-10): ")

guess2 = input("exercise? (0 or 1): ")

guess3 = input("eat well (0 or 1): ")

guess4 = input("sleep scr (0-10): ")

guess5 = input("sensory overwhelm/anxiety scr (0-10): ")
#10 being high and 0 being low - how close are you to snapping? how tapped out are you? 

now = datetime.datetime.now()

#save results

save_path = "C:/Users/kelbla/Documents/Testing/python_training/hackerrank/"
outfile="mood.out"
completeName = os.path.join(save_path, outfile)         

sys.stdout = open(completeName, 'a')

print(now,',',guess1,',',guess2, ',', guess3, ',', guess4, ',', guess5  )
