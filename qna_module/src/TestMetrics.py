#!/usr/bin/env python
# coding: utf-8

from sklearn.metrics import confusion_matrix
from LoadCSV import LoadCSV
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


class TestMetrics(object):

    """ Genera matrix de confusión a partir del testeo """

    def __init__(self, content):
        self.content = content
        self.path = os.path.join('../input',content,'test')
        self.file_csv = LoadCSV(self.content).csv()

    
    def build_matrix(self):
        y_exp = list(self.file_csv['tag_esperado'])
        y_pred = list(self.file_csv['tag_obtenido'])
        labels = self.file_csv.tag_esperado.values
        conf_matrix = confusion_matrix(y_exp, y_pred, labels= labels)
        return conf_matrix


    def build_conf_matrix(self):        
        plt.clf()
        cm = self.build_matrix()
        plt.imshow(cm, cmap=plt.cm.Blues)
        classNames = self.file_csv.tag_esperado.values
        plt.title('QnA - Test')
        plt.xlabel('Tag obtenido')
        plt.ylabel('Tag esperado')
        tick_marks = np.arange(len(classNames))
        plt.xticks(tick_marks, classNames, rotation=90)
        plt.yticks(tick_marks, classNames)
        plt.tight_layout()
        name_file = os.path.join(self.path, 'confusion_matrix.jpg')
        plt.savefig(name_file)
        print("La matriz de confusión se ha guardado en ", name_file)

    def check_labels(self):
        if not self.file_csv.tag_esperado.isna().any() or self.file_csv.tag_esperado.isnull().any():
            return True
        else:
            return False


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('content', help='Contenido para crear la base de datos', default=False)
    args = parser.parse_args()

    TestMetrics(args.content).build_conf_matrix()