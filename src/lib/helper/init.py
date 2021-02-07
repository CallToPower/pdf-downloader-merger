#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''Helper functions'''

import yaml
import logging

def get_ascii_art_banner():
    """Returns the ASCII-art banner

    :return: ASCII-art banner
    """
    return r"""

 / \-----------------------------, 
 \_,|                            | 
    |    PDF Downloader/Merger   | 
    |  ,---------------------------
    \_/__________________________/ 
    Copyright (C) 2021 Denis Meyer
"""

def load_cfg(filename):
    '''
    Loads the configuration from aa external file
    '''
    with open(filename, 'r') as yaml_config_file:
        cfg = yaml.load(yaml_config_file, Loader=yaml.FullLoader)
    return cfg


def initialize_logger(cfg):
    '''
    Initializes the logger

    :param cfg: The configuration
    '''
    if cfg['logging']['level'] == 'fatal':
        level = logging.FATAL
    elif cfg['logging']['level'] == 'error':
        level = logging.ERROR
    elif cfg['logging']['level'] == 'info':
        level = logging.INFO
    elif cfg['logging']['level'] == 'debug':
        level = logging.DEBUG
    else:
        level = logging.INFO

    logging.basicConfig(level=level,
                        format=cfg['logging']['format'],
                        datefmt=cfg['logging']['date_format'])
