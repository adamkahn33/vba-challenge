#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:17:21 2020

@author: akahn20
"""
    
user = "y"

while user == "y":
    askuser = int(input("How many numbers?"))
    for x in range(askuser+1):
        print (x)
    user = input("Wanna play again: (y)es (n)o")
    
    while user == "y":
        askuser2 = int(input("How many numbers?"))
        for y in range(askuser2+1):
             print(x + y)
        user = input("Wanna play again: (y)es (n)o")
        
            
    
else:
        print("Okay! Goodbye!")
    
    
