# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 14:56:11 2021

@author: Aditi Devgan
"""

#Q1
'''for i in range(100):
    j = 2**i
    print(j)'''
    
#Q2
num = int(input())
rev = 0
while num > 0:
    new = num%10
    rev = rev*10 + new
    num = num//10
print(rev)