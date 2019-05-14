#!/usr/bin/env python
# coding: utf-8

import yaml
from ConfigLoader import ConfigLoader


class BuildConfig(object):

    """ Actualiza archivo de configuración config.yml """

    def __init__(self, content):
        self.config_path = ConfigLoader(content).config_path
        self.config_file_stream = open(self.config_path, "r")
        self.config = yaml.load(self.config_file_stream)

    def update(self, section, param, new_value):
        self.config[section][param] = new_value
        with open(self.config_path, "w") as f:
            yaml.dump(self.config, f, default_flow_style=False)
