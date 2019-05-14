#!/usr/bin/env python
# coding: utf-8

import json

class Content(object):

  """ Formatea el contenido """

  def pretty_print(self,content):
    return json.dumps(json.loads(content), ensure_ascii=False, indent=4)
  
  
  def pretty_print_json(self,content):
    return json.loads(content, encoding='utf-8')