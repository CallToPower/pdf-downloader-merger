#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''Merge functions'''

import logging
import os
from pathlib import Path

from PyPDF2 import PdfFileMerger

def merge(outdirpath, name, files):
    merger = PdfFileMerger()
    for pdf in files:
        logging.debug('Appending file "{}"'.format(pdf))
        merger.append(open(pdf, 'rb'))

    out_file = Path('{}/{}-all.pdf'.format(outdirpath, name))

    if os.path.isfile(out_file):
        logging.debug('Deleting output file "{}"'.format(out_file))
        os.remove(out_file)

    logging.info('Writing output file "{}"'.format(out_file))
    with open(out_file, 'wb') as fout:
        merger.write(fout)
    merger.close()
