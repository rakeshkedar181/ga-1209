# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 12:47:42 2020

@author: RAKESH
"""
import re

class PreprocessDoc:
    """
    Module for preprocessing documents/articles 
    """
    def removeSplChar(self,text):
        """
         Remove special characters
         
         Input:
             text:string
         Output:
             modified text:string
        """
        filteredText = re.sub(',|;|#|$','',text)
        return filteredText
        pass
    
    def convertToLower(self,text):
        return text.lower()
    
    def tokenizeArticle(text):
        """
        Tokenize the articles
        
        Input:
            text:string
        Output:
            tokens/ list of words
        """
        pass
    
    def removeStopWords(words_list):
        """
        Remove stop words
        
        Input:
            list of words
        Output:
            Modified list of words after removing
        """
        pass