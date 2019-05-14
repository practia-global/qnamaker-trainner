#!/usr/bin/env python
# coding: utf-8

import yaml
import os

class ConfigLoader(object):

    """ Carga el archivo de configuración """

    def __init__(self,content):
        self.config_path = os.path.join('../input',content,'config.yml')
        self.__config_file_stream = open(self.config_path, "r")
        self.__config = yaml.load(self.__config_file_stream)
        self.__config_file_stream.close()

    def get_param(self, section_name, param_name):
        return self.__config[section_name][param_name]

    def get_section(self, section_name):
        return self.__config[section_name]
