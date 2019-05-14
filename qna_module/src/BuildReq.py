#!/usr/bin/env python
# coding: utf-8

import os
import json
from LoadFiles import Load


class BuildReq(object):

  """ Genera y formatea el contenido para armar la base de conocimiento """

  def __init__(self, content, name, source):
    self.content = content
    self.name = name
    self.source = source
    self.path = os.path.join('../input/',content)


  def build_entry(self, questions, answers):
    qnaList=[]
    mapper={'none':-1}
    i = 1
    for k in questions.keys():
      entry = {"id":i,
                "answer": answers[k],
                "source": self.source,
                "questions": questions[k],
                "metadata": [{
                    "name":"category",
                    "value":"api"
                }]}
      mapper[k]=i
      qnaList.append(entry)
      i += 1
    mapper_file = os.path.join(self.path, 'ID_mapper.json')
    with open(mapper_file, 'w') as f:
      json.dump(mapper, f, ensure_ascii=False, indent=4)
    return qnaList


  def build_req(self):
    req = {"name": self.name,
          "qnaList":[],
          "urls":[],
          "files":[]}

    if os.path.exists(self.path):

      cont = Load(self.content)

      pregs = cont.load_questions()
      if len(pregs) != 0:
        rttas = cont.load_answers()
        qnaList = self.build_entry(pregs, rttas)
        req['qnaList'] = qnaList

      urls = cont.load_url()
      req['urls'] = urls

      files = cont.load_file()
      req['files'] = files

      self.save_req(req)
      
    return req


  def save_req(self, req):
    file = os.path.join(self.path,'trainning.json')
    with open(file, 'w') as f:
      json.dump(req, f, ensure_ascii=False, indent=4)



if __name__ == "__main__":

  import argparse
  import json

  parser = argparse.ArgumentParser()
  parser.add_argument('content', help='Contenido para armar el req', type=str)
  parser.add_argument('--name','-n', help='Nombre de la base de conocimiento', type=str, default='New KB')
  parser.add_argument('--source','-s', help='Fuente de la base de conocimiento', type=str, default='Custom Editorial')
  args = parser.parse_args()

  content = BuildReq(args.content, args.name, args.source).build_req()
  
  print(json.dumps(content,ensure_ascii=False, indent=4))