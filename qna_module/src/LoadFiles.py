#!/usr/bin/env python
# coding: utf-8

import os
import json
import re


class Load(object):

  """ Carga el contenido """

  def __init__(self, content):
    self.path = os.path.join('../input',content)


  def load_questions(self):
    q_path = os.path.join(self.path, 'pregs')
    q = {}
    if os.path.exists(q_path):
      for f in os.listdir(q_path):
        p = os.path.join(q_path, f)
        with open(p,'r') as f:
            pregs = json.load(f)
        q.update(pregs)
    return q


  def load_answers(self):
    a_path = os.path.join(self.path, 'rttas')
    a = {}
    if os.path.exists(a_path):
      for f in os.listdir(a_path):
        p = os.path.join(a_path, f)
        key = re.sub('.txt','',f)
        with open(p,'r') as f:
            rttas = f.readlines()
            rttas = [r.strip() for r in rttas]
            rttas = ' '.join(rttas)
        a[key]=rttas
    return a


  def load_url(self):
    u_path = os.path.join(self.path, 'urls.txt')
    if os.path.isfile(u_path):
      print("Loading urls file")
      with open(u_path,'r') as f:
        url = f.readlines()
    else:
      print("No urls file")
      url = []
    return url


  def load_file(self):
    f_path = os.path.join(self.path, 'files.txt')
    if os.path.isfile(f_path):
      print("Loading files file")
      with open(f_path,'r') as f:
        file = f.readlines()
    else:
      print("No file with files")
      file = []

    return file


if __name__ == "__main__":

  import argparse

  parser = argparse.ArgumentParser()
  parser.add_argument('content', help='Contenido a cargar',type=str)
  args = parser.parse_args()

  contenido = Load(args.content).load_questions()
  
  print(contenido)