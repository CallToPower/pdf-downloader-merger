#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

'''Create functions'''

import logging
import os

import fpdf

def create_frontpage(outfile, fullname, descriptions, address):
    if os.path.isfile(outfile):
        logging.debug('Deleting file "{}"'.format(outfile))
        os.remove(outfile)

    pdf = fpdf.FPDF('P', 'mm', 'A4')
    pdf.add_page()
    pdf.set_font('Arial', 'B', size=16)
    ln = 1
    pdf.cell(250, 20, txt='{}'.format(fullname), ln=ln, align="L")
    ln = ln + 1
    pdf.set_font('Arial', size=12)
    for description in descriptions:
        pdf.cell(200, 10, txt='{}'.format(description), ln=ln, align="L")
        ln = ln + 1
    pdf.set_font('Arial', size=12)
    pdf.cell(200, 20, txt='{}'.format(address), ln=ln, align="R")
    pdf.output(outfile)
