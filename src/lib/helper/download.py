#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''Download functions'''

import logging
import requests
import os
from pathlib import Path

def download(address, fname, subdirpath, force=False):
    logging.debug('Downloading file "{}" from URL "{}"'.format(fname, address))

    save_to = Path('{}/{}'.format(subdirpath, fname))

    if not force and os.path.isfile(save_to):
        logging.debug('File already downloaded, not downloading again')
        return

    if not fname.endswith('.pdf'):
        logging.warn('File "{}" does not seem to be a PDF file'.format(fname))

    url = '{}/{}'.format(address, fname)
    r = requests.get(url, stream=True)
    if not r.status_code == 200:
        logging.error('Failed to download file "{}" from "{}"'.format(save_to, url))
        return

    with open(save_to, 'wb') as f:
        logging.debug('Saving file to "{}"'.format(save_to))
        f.write(r.content)
