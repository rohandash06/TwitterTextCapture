# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 23:39:56 2018

@author: rdas3
"""

import operator


def total_Users():
    INPUT_FILE = input("Enter the path of the input file located: ")
    INPUT_FILE_PATH = INPUT_FILE+ '.txt'
    x = input("Enter a number: ")
    n = int(x)
    OUTFILE = r'C:\Users\rdas3\Desktop\Docs'
    OUTPUT_FILE_PATH = OUTFILE + '.txt'
    with open (INPUT_FILE_PATH, encoding = "latin-1") as my_File:
        tweet=my_File.readlines()
    L = {}
    for dat in tweet:
       
        fileTemp1 = dat.split()
        if fileTemp1[0] in L:
            L[fileTemp1[0]] +=1
        else:
            L[fileTemp1[0]] = 1
    L = sorted(L.items(), key = operator.itemgetter(1), reverse = True)
 
    output_File = open(OUTPUT_FILE_PATH, 'w', encoding = 'utf-8')
	   
    output_File.write("The top"+ x +"users who have tweeted the most in the timeframe: \n")
    for i in range (0,n):
        output_File.write("User Name " + L[i][0] + "\n\n")
        
    output_File.close
total_Users()