#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

##############################################################################
#
# @file: unwind_the_binding.py
# @author: David BLACK    GH: @bballdave025
#          based on (and maybe only using)
#          https://stackoverflow.com/a/47877930/6505499
#          from @kateryna
# @since: 2024-01-22
#
# @requirements :
# % pip install --upgrade pip
# % pip install --upgrade pymupdf
# % pip install tqdm
#
#  This script will quickly take the PDFs in  fromdir  and convert them into
#+ PNGs in the  outdir .
#+ This is part of classifying Manuscript document images for a
#+ paper/presentation at the Family History Technology Conference
#+ and for academia.edu
#
##############################################################################

import os
import fitz
from tqdm import tqdm

#just_one_pdf_at_a_time = True

fromdir = "C:/Users/Anast/Desktop/_waiting_pdfs"
outdir = "C:/Users/Anast/Desktop/_waiting_wild_imgs_out"

for each_path in os.listdir(fromdir):
  if ".pdf" in each_path:
    doc = fitz.Document((os.path.join(fromdir, each_path)))
    
    for i in tqdm(range(len(doc)), desc="pages"):
      for img in tqdm(doc.get_page_images(i), desc="page_images"):
        xref = img[0]
        image = doc.extract_image(xref)
        pix = fitz.Pixmap(doc, xref)
        pix.save(os.path.join(outdir,
                              "%s_p%s-%s.png" % (each_path[:-4], i, xref))
        )
      ##endof:  for img
    ##endof:  for i in tqdm
  ##endof:  if ".pdf"
##endof:  for each_path

#if just_one_pdf_at_a_time:
## We're printing out our progress to stdout, why not do
print("Done!")
