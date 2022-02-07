#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 22:40:41 2021

@author: tavastm1
"""
import os
import xlsxwriter

path = 'prompts/GamesAsArt/'
thinking = True
if thinking == True:
    file_start= 'thinking_game_'
    naming = 'thinking'
else:
    file_start= 'game_'
    naming = ''
file_end = 'davinci.txt'

examples_list = []
index_list = []
for file in os.listdir(path):
    if file.startswith(file_start) and file.endswith(file_end):
        examples_list.append(open(path + file, "r").read())
        index_list.append(file)
        print(file)
               
print(len(examples_list))

AllGames = xlsxwriter.Workbook(f'prompts/GamesAsArt/AllGames_{naming}.xlsx')
AllGamess = AllGames.add_worksheet()
row = 0

for i in range(len(examples_list)):
    column = 0
    AllGamess.write(row, column, index_list[i])
    column = 1
    AllGamess.write(row, column, examples_list[i])
    row += 1
AllGames.close()


