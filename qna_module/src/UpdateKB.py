# -*- coding: utf-8 -*-

import http.client, urllib.parse, json, time
from ConfigLoader import ConfigLoader
from Content import Content
from BuildChanges import BuildChanges
import re
from BuildConfig import BuildConfig

class UpdateKB(object):

    """ Actualiza una base de conocimiento ya existente """

    def __init__(self, content):
        self.content = content
        self.config = ConfigLoader(self.content)
        self.qna1key = self.config.get_section('qna1key')
        self.kb = self.config.get_param('publish','kb')
        self.host = self.config.get_section('main_host')
        self.service = self.config.get_section('service')
        self.method = self.config.get_param('publish','method')


    def update_kb(self, path, req):
        print('Calling ' + self.host + path + '.')
        headers = {
            'Ocp-Apim-Subscription-Key': self.qna1key,
            'Content-Type': 'application/json',
            'Content-Length': len(req)
        }
        conn = http.client.HTTPSConnection(self.host)
        conn.request ("PATCH", path, req, headers)
        response = conn.getresponse ()
        return response.getheader('Location'), response.read ()


    def check_status(self, path):
        print('Calling ' + self.host + path + '.')
        headers = {'Ocp-Apim-Subscription-Key': self.qna1key}
        conn = http.client.HTTPSConnection(self.host)
        conn.request("GET", path, None, headers)
        response = conn.getresponse ()
        # If the operation is not finished, /operations returns an HTTP header named
        # 'Retry-After' with the number of seconds to wait before querying the operation again.
        return response.getheader('Retry-After'), response.read ()


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

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('content', help='Contenido para crear la base de datos', default=False)
    parser.add_argument('--name', '-n', help='Nombre para la base de conocimiento', default=False)
    parser.add_argument('--source','-s', help='Fuente de la base de conocimiento', default='Custom Editorial')
    args = parser.parse_args()

    KB = UpdateKB(args.content)

    req = BuildChanges(content=args.content, name=args.name, source=args.source).build_all()
    # Convert the request to a string.
    content = json.dumps(req)

    # Builds the path URL.
    path = KB.service + KB.method + KB.kb

    # Retrieve the operation ID to check status, and JSON result.
    operation, result = KB.update_kb(path, content)

    # Print request response in JSON with presentable formatting.
    print(Content().pretty_print(result))

    KB.get_status(operation)