#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''File functions'''

import logging
import os
import shutil

def remove_directory(dirpath):
    logging.debug('Removing local download directory "{}"'.format(dirpath)) # Path.cwd()
    if dirpath.exists() and dirpath.is_dir():
        shutil.rmtree(dirpath)

def create_directory(dirpath):
    logging.debug('Creating local download directory "{}"'.format(dirpath))
    try:
        os.makedirs(dirpath)
    except Exception as e:
        logging.error('Could not create directory "{}": "{}"'.format(dirpath, e))
        raise e
    else:
        logging.debug('Successfully created directory "{}"'.format(dirpath))
