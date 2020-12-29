# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:48:50 2020

@author: RAKESH
"""
import yaml

class SummarizerDoc:
    
    def __init__(self):
        with open('../config/config.yml','r') as fl:
            self.config = yaml.safe_load(fl)
        
    
    def loadDocs(self,filePath):
        with open(filePath,'r') as fl:
            text = fl.read()
        return text
        pass
    
    def loadConfig(self):
        pass
    
    def splitSentences(self,text):
        """
        Split the paragraph into an array of sentences
        
        Input:
            text:string
        Output:
            sentences: a list of string
        """
        sentences = text.split('.')
        return sentences
        pass
    
    def groupSentences(self,sentences):
        firstSent, restOfSent = sentences[0], sentences[1:]
        return firstSent, restOfSent
    
    def firstSentExtractor(self):
        pass
    
    def findNumWords():
        pass
    
    def findTopSentences():
        pass
    
    def sentenceCombiner():
        pass
    
summarizerObj = SummarizerDoc()
summarizerObj.loadConfig()