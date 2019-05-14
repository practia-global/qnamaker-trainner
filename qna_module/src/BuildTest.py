#!/usr/bin/env python
# coding: utf-8


import os
from LoadCSV import LoadCSV


class BuildTest(object):
    
    """ Genera set de testeo """

    def __init__(self, content, top):
        self.file = LoadCSV(content)
        self.input = self.file.Questions()
        self.top = top
        

    def Test(self):
        test=[{'question':p, 'top':self.top} for p in self.input['Preguntas']]
        return test
        

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('content', help='Contenido para crear el testset')
    parser.add_argument('--top','-t', help='Cantidad de respuestas a considerar', default=1, type=int)
    args = parser.parse_args()

    print(BuildTest(args.content,args.top).Test())