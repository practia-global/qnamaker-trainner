#!/usr/bin/env python
# coding: utf-8

import http.client, urllib.parse
import json
import time
import re
import argparse
from ConfigLoader import ConfigLoader
from BuildReq import BuildReq
from Content import Content
from BuildConfig import BuildConfig

  
class CreateKB(object):

  """ Crea una nueva base de conocimiento """

  def __init__(self, content):
    self.content = content
    self.config = ConfigLoader(self.content)
    self.qna1key = self.config.get_section('qna1key')
    self.host = self.config.get_section('main_host')
    self.service = self.config.get_section('service')
    self.method = self.config.get_param('create','method')
    

  def check_status(self, path):
    print('Calling ' + self.host + path + '.')
    headers = {'Ocp-Apim-Subscription-Key': self.qna1key}
    conn = http.client.HTTPSConnection(self.host)
    conn.request("GET", path, None, headers)
    response = conn.getresponse ()
    # If the operation is not finished, /operations returns an HTTP header named Retry-After
    # that contains the number of seconds to wait before we query the operation again.
    return response.getheader('Retry-After'), response.read ()


  def create_kb(self, path, req):
    print('Calling ' + self.host + path + '.')
    headers = {
    'Ocp-Apim-Subscription-Key': self.qna1key,
    'Content-Type': 'application/json',
    'Content-Length': len(req)
    }
    conn = http.client.HTTPSConnection(self.host)
    conn.request ("POST", path, req, headers)
    response = conn.getresponse ()
    # /knowledgebases/create returns an HTTP header named Location that contains a URL
    # to check the status of the operation in creating the knowledge base.
    return response.getheader('Location'), response.read ()


  def get_status(self, operation):
    done = False
    while False == done:
      path = self.service + operation
      # Gets the status of the operation.
      wait, status = self.check_status(path)
      # Print status checks in JSON with presentable formatting
      print(Content().pretty_print(status))
      # Convert the JSON response into an object and get the value of the operationState field.
      state = json.loads(status)['operationState']
      # If the operation isn't finished, wait and query again.
      if state == 'Running' or state == 'NotStarted':
        print('Waiting ' + wait + ' seconds...')
        time.sleep(int(wait))
      else:
        kb = Content().pretty_print_json(status)
        kb_id = kb['resourceLocation']
        kb_id = re.sub('/knowledgebases/','',kb_id).strip()
        write_conf = BuildConfig(self.content)
        write_conf.update('publish','kb', kb_id)
        done = True # request has been processed, if successful, knowledge base is created


if __name__ == '__main__':

  parser = argparse.ArgumentParser()
  parser.add_argument('content', help='Contenido para crear la base de datos', default=False)
  parser.add_argument('--name', '-n', help='Nombre para la base de conocimiento', default='New KB',type=str)
  parser.add_argument('--source','-s', help='Fuente de la base de conocimiento', default='Custom Editorial')
  args = parser.parse_args()

  KB = CreateKB(args.content)

  req = BuildReq(content=args.content, name=args.name, source=args.source).build_req()

  # Convert the request to a string.
  content = json.dumps(req)

  # Builds the path URL.
  path = KB.service + KB.method

  # Retrieve the operation ID to check status, and JSON result
  operation, result = KB.create_kb(path, content)

  # Print request response in JSON with presentable formatting<<
  print(Content().pretty_print(result))

  KB.get_status(operation)