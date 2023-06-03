#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabienfrfr
"""

import random
import nltk

nltk.download('words')

class Subjective() :
    def __init__(self) : 
        # question structure ['fstring', pivot value]
        self.sentence = [['I like {thing}.', 1],
                         ['I love {thing}.', 1],
                         ['I hate {thing}.', 1],
                         ['I prefer {thing} compared to {stuff}.', 1],
                         ['{thing} is beautiful.', 2],
                         ['{thing} is big.', 2],
                         ['{thing} is small.',2],
                         ['{thing} is ugly.', 2]]
        
    def subject(self):
        pass