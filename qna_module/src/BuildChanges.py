#!/usr/bin/env python
# coding: utf-8

import os
import json
from LoadFiles import Load
from ConfigLoader import ConfigLoader


class BuildChanges(object):

    """ Genera y da formato al archivo para subir modificaciones a una base de conocimiento """
  
    def __init__(self, content, name, source):
        self.content = content
        self.name = name
        self.source = source
        self.path = os.path.join('../input/',content)
        self.path_modifications = os.path.join(self.path, 'modificaciones')
        self.path_old_kb = os.path.join(self.path,'trainning.json')
        self.old_kb_stream = open(self.path_old_kb,'r')
        self.old_kb = json.load(self.old_kb_stream)
        self.path_old_mapper = os.path.join(self.path,'ID_mapper.json')


    def load_url(self):
        route = os.path.join(self.content, 'modificaciones', 'agregar')
        Load(route).load_url()

    def qnaList(self):
        qnaList = []
        route = os.path.join(self.content, 'modificaciones', 'agregar')
        with open(self.path_old_mapper, 'r') as f:
            new_mapper = json.load(f)
        questions = Load(route).load_questions()
        answers = Load(route).load_answers()
        i = max(new_mapper.values())+1
        for k in questions.keys():
            entry = {"id":i,
                    "answer": answers[k],
                    "source": self.source,
                    "questions": questions[k],
                    "metadata": [{
                        "name":"category",
                        "value":"api"
                    }]}
            new_mapper[k]=i
            qnaList.append(entry)
            i += 1
        with open(self.path_old_mapper, 'w') as f:
            json.dump(new_mapper, f, ensure_ascii=False, indent=4)
        return qnaList


    def build_add(self):
        add = {'qnaList': self.qnaList(),
                'urls': self.load_url()}
        return add


    def build_update(self):
        update = {}
        if self.name != False:
            update['name']= self.name
        else:
            update['name']= self.old_kb['name']
        return update


    def build_delete(self):
        delete = {'ids':[]}
        to_delete = os.path.join(self.path_modifications, 'borrar.json')
        if os.path.exists(to_delete):
            with open(to_delete, 'r') as f:
                ids = json.load(f)
            delete['ids'] = delete['ids'] + ids['borrar']
            self.delete_id_from_mapper(ids['borrar'])
        return delete


    def build_all(self):
        req = {'add': self.build_add(),
                'update': self.build_update(),
                'delete': self.build_delete()
                }
        return req

    
    def delete_id_from_mapper(self, ids):
        new_mapper = {}
        with open(self.path_old_mapper, 'r') as f:
            mapper = json.load(f)
        for k, v in mapper.items():
            if v not in ids:
                new_mapper[k] = v
        with open(self.path_old_mapper, 'w') as f:
            json.dump(new_mapper, f, ensure_ascii=False, indent=4)

