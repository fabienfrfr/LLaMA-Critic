#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabienfrfr
"""
import random 
from sympy import *
from scipy.optimize import fsolve
from scipy.integrate import odeint

class Math() :
    def __init__(self) :
        # question structure ['fstring', pivot value]
        self.assertion = [["Let {equality}. What is {variable}? It's {solution}.", -2],
                          ["Let {equality}. Calculate {variable}. It's {solution}.", -2],
                          ["Suppose {equality}. What is {variable}? It's {solution}.", -2],
                          ["Suppose {equality}. Calculate {variable}. It's {solution}.", -2],
                          ["What is {variable} in {equality}? It's {solution}.", -2],
                          ["Solve {equality} for {variable}. It's {solution}.", -2],
                          ["Find {variable} such that {equality}. It's {solution}.", -2],
                          ["Find {variable}, given that {equality}. It's {solution}.", -2],
                          ["Determine {variable} so that {equality}. It's {solution}.", -2],
                          ["Determine {variable}, given that {equality}. It's {solution}.", -2],
                          ["Solve {equality}. It's {solution}.", -2]]
    
    def algebra(self):
        pass
    
    def arithmetic(self):
        pass
    
    def calculus(self):
        pass
    
    def comparison(self):
        pass
    
    def measurement(self):
        pass
    
    def numbers(self):
        pass
    
    def polynomial(self):
        pass
    
    def probability(self):
        pass