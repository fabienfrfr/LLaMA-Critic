#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabienfrfr
"""

from semantics import Semantics
import numpy as np
import random

class AssertionGenerator() :
    def __init__(self) :
        # math
        #
        # semantics
        semantics = Semantics()
        # subjective
        #
        # all
        self.assertor = [None, semantics, None]
        # assertion choice parameter
        self.weight = [0., 1., 0.]
    
    def generate(self, N_sentence=8) :
        assertions = ''
        truths = [-1]
        for i in range(N_sentence):
            # find index
            idx = random.choices([0,1,2], weights=self.weight)[0]
            assertor = self.assertor[idx]
            # generate
            s,p,t = assertor.generate(N_sentence)
            # define thruth list (-1 start, 0.66 undefined, [0,0.5,1] if [false, subjective, true]) --> reflexions needed
            token = (2./3) * np.ones(len(s.split(' ')))
            token[:p[0]+1] = -1
            token[p[1]:] = float(t)
            # complete
            assertions += ' ' + s
            truths += token.tolist()
        return assertions, truths
    
    def rollsentence(self):
        n = 0
        actual_token = -1
        if actual_token == -1 :
            n += 1
        pass
    
### basic exemple
if __name__ == '__main__' :
    assertor = AssertionGenerator()
    a, t = assertor.generate(16)
    print(a,t)