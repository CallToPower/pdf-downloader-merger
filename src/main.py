#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''Main'''

import logging
import os
from pathlib import Path
from time import sleep

from lib.helper.init import initialize_logger, load_cfg, get_ascii_art_banner
from lib.helper.file import remove_directory, create_directory
from lib.helper.download import download
from lib.helper.merge import merge
from lib.helper.create import create_frontpage

CONFIG_FILE = os.path.dirname(os.path.abspath(__file__)) + '/settings.yaml'


if __name__ == '__main__':
    cfg = load_cfg(CONFIG_FILE)
    initialize_logger(cfg)

    logging.info(get_ascii_art_banner())

    out_dir = cfg['files']['out_directory']

    if cfg['files']['download']['active']:
        dirpath = Path(out_dir)
        if cfg['files']['download']['force']:
            remove_directory(dirpath)
            sleep(0.05) # Wait for the OS to remove dir
        if not os.path.isdir(dirpath):
            create_directory(dirpath)

        logging.info('Downloading files...')
        for address in cfg['files']['addresses']:
            name = cfg['files']['addresses'][address]['name']
            subdirpath = Path('{}/{}'.format(out_dir, name))
            if not os.path.isdir(subdirpath):
                create_directory(subdirpath)
            logging.info('Downloading from address "{}" ( {} )'.format(name, address))
            nr_files = 0
            for fname in cfg['files']['addresses'][address]['files']:
                nr_files = nr_files + 1
                download(address, fname, subdirpath, force=cfg['files']['download']['force'])
                logging.info('Progress: {}/{} files downloaded'.format(nr_files, len(cfg['files']['addresses'][address]['files'])))
        logging.info('Done')

    if cfg['files']['merge']['active']:
        logging.info('Merging files...')
        for address in cfg['files']['addresses']:
            name = cfg['files']['addresses'][address]['name']
            outdirpath = Path('{}/{}'.format(out_dir, name))

            if cfg['files']['merge']['create_frontpage']:
                logging.info('Creating frontpage')
                frontpagefile = Path('{}/{}-frontpage.pdf'.format(outdirpath, name))
                fullname = cfg['files']['addresses'][address]['fullname']
                descriptions = cfg['files']['addresses'][address]['descriptions']
                create_frontpage(frontpagefile, fullname, descriptions, address)
            subdirpath = Path('{}/{}'.format(out_dir, name))
            if not os.path.isdir(subdirpath):
                raise Exception('Directory "{}" does not exist'.format(subdirpath))
            logging.info('Merging files from directory "{}"'.format(name))
            files = [Path('{}/{}'.format(subdirpath, f)) for f in cfg['files']['addresses'][address]['files']]
            if cfg['files']['merge']['create_frontpage']:
                files = [frontpagefile] + files
            merge(outdirpath, name, files)
        logging.info('Done')
    logging.info('Thanks for using "PDF Downloader/Merger"')
