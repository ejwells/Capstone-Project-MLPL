# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 21:22:27 2016

@author: titou
"""

fileName='input.txt'
outputeFile='output.txt'

f=open( 'inputFile.txt', 'r' )
out=open(outputeFile,'w')
result=dict()
for line in f :
    words = line.split()
    for word in words[1:-1]:
        string="%s %s \n" % (words[0],word)
        out.write(string)
        
        
f.close()
out.close()
