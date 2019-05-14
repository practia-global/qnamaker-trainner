#!/usr/bin/env python
# coding: utf-8

import json
import os


class LoadJSON(object):

    """ Carga archivos .json """

    def __init__(self, content):
        self.path = os.path.join('../input',content)

    
    def output(self):
        file = os.path.join(self.path, 'test', 'output.json')
        with open(file, 'r') as f:
            file = json.load(f)
        return file


    def mapper(self):
        file = os.path.join(self.path, 'ID_mapper.json')
        with open(file, 'r') as f:
            file = json.load(f)
        return file