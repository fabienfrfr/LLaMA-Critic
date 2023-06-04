#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: fabienfrfr
"""

import random
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('words')

import gensim
import gensim.downloader as api

# utils
import re
def get_variable_names(fstring):
    pattern = r'{([a-zA-Z_][a-zA-Z0-9_]*)}'
    matches = re.findall(pattern, fstring)
    return matches

class Semantics() :
    def __init__(self) :
        self.context = ["concept", "context", "idea", "category", "class"]
        # question structure ['fstring', pivot value]
        self.simimilarity = [["{word1} and {word2} are part of the same {context}.", [0,-2]],
                             ["{word1} and {word2} belong to the same {context}.", [0,-2]],
                             ["{word1} is close to {context} of {word2}.", [0,-2]],
                             ["{word1} is near to {context} of {word2}.", [0,-2]],
                             ["{word1} have similarity of {word2}.", [0,-2]],
                             ["{word1} is soon of sens of {word2}.", [0,-2]],
                             ["the {context} distance between {word1} and {word2} is small.", [0,-2]]]
        self.familiarity = [["{a} is include to {A}.", [0,-2]],
                            ["{a} is an element of {A}.", [0,-2]],
                            ["{A} includes {a}.", [0,-2]],
                            ["{A} contains {a}.", [0,-2]],
                            ["{a} is a member of {A}.", [0,-2]],
                            ["{a} is an example of {A}.", [0,-2]]]
        # model (https://github.com/RaRe-Technologies/gensim-data)
        path = api.load('glove-wiki-gigaword-100', return_path=True)
        self.w2v_model = gensim.models.KeyedVectors.load_word2vec_format(path, binary=False)
        # word
        self.w2v_words =  [i for i in list(self.w2v_model.key_to_index.keys()) if len(i)>2]
        self.nltk_words = [i for i in nltk.corpus.words.words() if len(i)>2]
    
    def wordDistance(self, N_sentence=2):
        word1 = random.choice(self.w2v_words)
        # true of false 
        P = 1./(2**N_sentence)
        truth = random.choices([True, False], weights=[1-P, P])[0]
        # find word2
        if truth :
            sims_word1 = self.w2v_model.most_similar(word1, topn=3)
            word2 = random.choices([s[0] for s in sims_word1])[0]
        else :
            unsims_word1 = self.w2v_model.most_similar(negative=[word1], topn=3)
            word2 = random.choices([s[0] for s in unsims_word1])[0]
        # sentence
        idx = random.randint(0, len(self.simimilarity)-1)
        sentence, pivot = self.simimilarity[idx]
        if "context" in get_variable_names(sentence) :
            context = random.choices(self.context)[0]
            sentence = sentence.format(word1=word1, word2=word2, context=context)
        else :
            sentence = sentence.format(word1=word1, word2=word2)
        # evaluate
        return sentence, pivot, truth

    def wordExtension(self, N_sentence=2):
        a = random.choice(self.nltk_words)
        # true of false 
        P = 1./(2**N_sentence)
        truth = random.choices([True, False], weights=[1-P, P])[0]
        # find hyperonym
        A = []
        for syn in nltk.corpus.wordnet.synsets(a):
            for hypernym in syn.hypernyms():
                for lem in hypernym.lemmas():
                    A.append(lem.name())
        if type(A) == list and len(A) > 0 : A = A[0]
        else : 
            # find hyponym
            A = a
            a = A
        # sentence
        idx = random.randint(0, len(self.familiarity)-1)
        sentence, pivot = self.familiarity[idx]
        sentence = sentence.format(a=a, A=A)
        # evaluate
        truth = True # not done yet
        return sentence, pivot, truth
    
    def generate(self, N_sentence=2):
        if random.choice([True, False]) :
            return self.wordDistance(N_sentence)
        else :
            return self.wordExtension(N_sentence)

### basic exemple
if __name__ == '__main__' :
    semantic = Semantics()
    for i in range(100):
        s,p,t = semantic.wordDistance()
        print(s,p,t)
        s,p,t = semantic.wordExtension()
        print(s,p,t)
