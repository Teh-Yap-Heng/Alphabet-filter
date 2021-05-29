# -*- coding: utf-8 -*-
"""
Created on Sat May 29 16:31:19 2021

@author: tehya
"""

def vowel(word):
    for x in word:
        if x in ['a','e','i','o','u']:
            word = word.replace(x, '')
    return word 

def consonant(word):
    for x in word:
        if x not in ['a','e','i','o','u']:
            word = word.replace(x, '')
    return word

print(vowel('hacker')) 
print(consonant('hacker')) 