#!/usr/bin/env python
# coding: utf-8

import http.client, urllib.parse, json, time
from Content import Content
from ConfigLoader import ConfigLoader
from GetEndpointKey import GetEndpoint
class PublishKB(object):
    
    """Publica una base de conocimiento ya creada """

    def __init__(self, content):
        self.content = content
        self.config = ConfigLoader(self.content)
        self.qna1key = self.config.get_section('qna1key')
        self.kb = self.config.get_param('publish','kb')
        self.host = self.config.get_section('main_host')
        self.service = self.config.get_section('service')
        self.method = self.config.get_param('publish','method')
        self.path = self.service + self.method + self.kb
        self.string = ''


    def publish_kb(self):
        print ('Calling ' + self.host + self.path + '.')
        headers = {
            'Ocp-Apim-Subscription-Key': self.qna1key,
            'Content-Type': 'application/json',
            'Content-Length': len(self.string)
        }
        conn = http.client.HTTPSConnection(self.host)
        conn.request ("POST", self.path, self.string, headers)
        response = conn.getresponse ()

        if response.status == 204:
            return json.dumps({'result' : 'Success.'})
        else:
            return response.read ()


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('content', help='Contenido para crear la base de datos', default=False)
    args = parser.parse_args()

    KB = PublishKB(args.content)
    result = KB.publish_kb()
    print (Content().pretty_print(result))

    GetEndpoint(args.content).get_endpoint()
