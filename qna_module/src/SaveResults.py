#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import os
import json
from LoadCSV import LoadCSV
from LoadJSON import LoadJSON

class SaveResults(object):

    """ Guarda los resultados del test en el .csv de preguntas """

    def __init__(self, content):
        self.content = content
        self.path = os.path.join('../input',content,'test')
        self.path_csv = os.path.join('../input',content,'test','pregs.csv')
        self.file_results = LoadJSON(self.content).output()
        self.file_csv = LoadCSV(self.content).csv()
        self.mapper = LoadJSON(self.content).mapper()


    def save(self):
        for a in self.file_results['answers']:
            condition = self.file_csv.Preguntas == a['question_asked']['question']
            self.file_csv.loc[condition, 'tag_obtenido'] = self.match_tag(a['id'])
            self.file_csv.loc[condition, 'score'] = a['score']
            self.file_csv.loc[condition, 'respuesta'] = a['answer']
        self.file_csv.to_csv(self.path_csv, index=False)
        print('El archivo ', self.path_csv, ' ha sido completado con los resultados obtenidos.')


    def match_tag(self, n):
        for k, v in self.mapper.items():
            if n == v:
                return k
        

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('content', help='Contenido para crear la base de datos', default=False)
    args = parser.parse_args()

    SaveResults(args.content).save()