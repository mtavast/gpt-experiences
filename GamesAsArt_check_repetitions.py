#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 10:45:11 2021

This script was used to change the filenames of already generated prompts, that had repetitions of over 10 character.

@author: tavastm1
"""
import re 
import os

path = 'prompts/GamesAsArt/'   
#file_start= 'thinking_game_'      # we have two versions of the query
file_start= 'game_'
file_end = 'davinci.txt'

# Find the game events
examples_list = []
index_list = []
for file in os.listdir(path):
    if file.startswith(file_start) and file.endswith(file_end):
        examples_list.append(open(path + file, "r").read())
        index_list.append(file)
        
# Stackoverflow question 9079797
# Finds repetitions in a string
def repetitions(s):
    r = re.compile(r"(.+?)\1+")
    for match in r.finditer(s):
        yield (match.group(1))

# Append files that have repetitions >10 to a list, later to be discarded
ToBeDiscarded = []  
FileNameList = []      
for i in range(len(examples_list)):
    temp = examples_list[i]
    temp2 = list(repetitions(temp))
    if len(temp2) > 0:
        for j in range(len(temp2)):
            if len(temp2[j]) > 10:  
                ToBeDiscarded.append(i)
                FileNameList.append(index_list[i])
                print(i, temp2[j])

# Discard the game events by renaming the files                
for file in os.listdir(path):
    if file.startswith('DISCARDED'):
       temp = (open(path + file, "r").read())
       print(file, temp)

for k in range(len(ToBeDiscarded)):
    temp3 = FileNameList[k]
    os.rename(f'prompts/GamesAsArt/{temp3}', f'prompts/GamesAsArt/DISCARDED_{temp3}')