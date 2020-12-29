# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:48:50 2020

@author: RAKESH
"""
import yaml
import numpy as np
from preprocessor import PreprocessDoc

class SummarizerDoc:
    
    def __init__(self):
        with open('/config/config.yml','r') as fl:
            self.config = yaml.safe_load(fl)
        
    
    def loadDocs(self,filePath):
        with open(filePath,'r',encoding='utf-8') as fl:
            text = fl.read()
        return text
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
    
    def findSentLength(self, text):
        return text.split()
    
    def findSentLengthArray(self,sentences):
        return [self.findSentLength(sent) for sent in sentences]
    
    def findTopSentences(self,sentLengths,sentences,n):
        sortedIdx = np.argsort(sentLengths)
        topnIdx = sortedIdx[-n:]
        topnSentences = [sentences[i] for i in topnIdx]
        return topnSentences
    
    def preprocessArticle(self,text):
        preprocessObj = PreprocessDoc()
        filteredText = preprocessObj.removeSplChar(text)
        filteredText = preprocessObj.convertToLower(filteredText)
        return filteredText
    
    def findSummary(self):
        filepath = self.config['data_path']['train_data']
        text = self.loadDocs(filepath)
        filteredText = self.preprocessArticle(text)
        sentences = self.splitSentences(filteredText)
        firstSent,restOfSent = self.groupSentences(sentences)
        sentLengths = self.findSentLengthArray(restOfSent)
        topnSentences  = self.findTopSentences(sentLengths,sentences,self.config['sentence_num'])
        allSentences = [firstSent] + topnSentences
        summary = '.'.join(allSentences)
        return summary
    
summarizerObj = SummarizerDoc()
summary = summarizerObj.findSummary()