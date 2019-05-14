# -*- coding: utf-8 -*-

import os
import json

class BuildUtteranceFile(object):

    def __init__(self):
        self.path = './pregs/'

    def text_list(self):
        text=[]
        for p in os.listdir(self.path):
            p = os.path.join(self.path, p)
            with open(p, 'r') as f:
                pregs = json.load(f)
            for k in pregs:
                text = text+pregs[k]
        return text

    def build_utterances(self):
        utterances = []
        utterances2 = []
        utterances3 = []
        for t in self.text_list():
            entry = {"text": t,
                    "intentName": "q_faq",
                    "entityLabels": []}
            if len(utterances) < 100:
                utterances.append(entry)
            else:
                if len(utterances2) < 100:
                    utterances2.append(entry)
                else:
                    utterances3.append(entry)
        with open('./utterances.json','w') as f:
            json.dump(utterances, f, ensure_ascii=False, indent=4)
        with open('./utterances2.json','w') as f:
            json.dump(utterances2, f, ensure_ascii=False, indent=4)
        with open('./utterances3.json','w') as f:
            json.dump(utterances3, f, ensure_ascii=False, indent=4)
        print('utt', len(utterances))
        print('utt2', len(utterances2))
        print('utt3', len(utterances3))



BuildUtteranceFile().build_utterances()