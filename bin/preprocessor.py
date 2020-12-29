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
    