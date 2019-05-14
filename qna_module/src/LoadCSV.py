#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import os


class LoadCSV(object):

    """ Carga archivos .csv """
    
    def __init__(self, content):
        self.path = os.path.join('../input',content,'test','pregs.csv')

    
    def Questions(self):
        df = pd.read_csv(self.path,usecols=['Preguntas'])
        return df


    def csv(self):
        df = pd.read_csv(self.path)
        return df