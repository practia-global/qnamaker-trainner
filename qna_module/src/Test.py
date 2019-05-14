#!/usr/bin/env python
# coding: utf-8

import http.client, urllib.parse, json, time
from ConfigLoader import ConfigLoader
from BuildTest import BuildTest
from Content import Content
from SaveResults import SaveResults
from TestMetrics import TestMetrics
import os


class GetAnswer(object):

	""" Testea la base de conocimiento """

	def __init__(self, content):
		self.content = content
		self.config = ConfigLoader(self.content)
		self.host = self.config.get_param('answer','host')
		self.endpoint_key = self.config.get_param('answer','endpointKey')
		self.kb = self.config.get_param('publish','kb')
		self.method = "/qnamaker/knowledgebases/" + self.kb + "/generateAnswer"
		self.path = '../input'


	def get_answers(self, req):
		print ('Calling ' + self.host + self.method + '.')
		headers = {
			'Authorization': 'EndpointKey ' + self.endpoint_key,
			'Content-Type': 'application/json',
			'Content-Length': len(req)
		}
		conn = http.client.HTTPSConnection(self.host)
		conn.request("POST", self.method, req, headers)
		response = conn.getresponse ()
		return response.read ()
	

	def check_answer(self,testset):
		output_file = os.path.join(self.path, self.content, 'test','output.json')
		output = {'answers':[]}
		print('Queries for testing: ',len(testset))
		i = 1
		for q in testset:
			print('Testing query nr.',i)
			req = json.dumps(q, ensure_ascii=True)
			result = self.get_answers(req)
			out = Content().pretty_print_json(result)
			for o in out["answers"]:
				o['question_asked']=q
				output['answers'].append(o)
			i += 1
		with open(output_file, 'w') as f:
			json.dump(output, f, ensure_ascii=False, indent=4)
		print('Testeo finalizado. Archivo de salida guardado en ', output_file)


if __name__ == '__main__':

	import argparse

	parser = argparse.ArgumentParser()
	parser.add_argument('content', help='Contenido que se desea testear testset')
	parser.add_argument('--top','-t', help='Cantidad de respuestas a considerar', default=1, type=int)
	args = parser.parse_args()

	question = BuildTest(args.content,args.top).Test()
	get = GetAnswer(args.content)
	get.check_answer(question)

	SaveResults(args.content).save()

	tm = TestMetrics(args.content)
	if tm.check_labels():
		tm.build_conf_matrix()
	else:
		print('El corpus de testeo no está etiquetado. Etiquetalo para poder generar una matrix de confusión.')