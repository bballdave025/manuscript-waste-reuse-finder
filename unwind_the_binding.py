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

# fromdir = "C:/Users/bballdave025/Desktop/_pdfs_for_images_-_workdir"
# outdir =  "C:/Users/bballdave025/Desktop/_imgs_from_pdfs_-_workdir"

# fromdir =   "D:/Datasets_and_Models/P2_MSS/_newest_pdfs"
# outdir =    "D:/Datasets_and_Models/P2_MSS/_newest_imgs_from_pdfs"

# fromdir =   "D:/Datasets_and_Models/P2_MSS/_pdfs_for_images_-_workdir"
# outdir =    "D:/Datasets_and_Models/P2_MSS/_imgs_from_pdfs_-_workdir"

fromdir = "C:/Users/bballdave025/Desktop/_pdfs_for_images_-_workdir"
outdir =  "C:/Users/bballdave025/Desktop/_imgs_from_pdfs_-_workdir"

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

if False:
  print(
"""
## Version that allows output, but runs more slowly
#(Below is the version that doesn't show output and runs more quickly.)


find . -type f -iname "*.png" > fnames.lst; \
echo -e "\n\n  $(date +'%s_%Y-%m-%dT%H%M%S%z') \n" | tee -a rename.out; \
find . -type f -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}";
echo;
echo "orig: ${orig}";
my_first=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*\)p\([0-9]\+\)[-][0-9]\+\([.]png\)$#\1#g'"'"');
echo "my_first: ${my_first}";
my_end=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\3#g'"'"');
echo "my_end: ${my_end}";
my_second=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\2#g'"'"');
echo "my_second: $my_second";
my_num=0;
my_unpad=$(echo "${my_second}+1" | bc);
echo "my_unpad: ${my_unpad}";
my_num=0;
if [ $my_unpad -lt 10 ]; then
  my_num="0000${my_unpad}";
elif [ $my_unpad -lt 100 ]; then
  my_num="000${my_unpad}";
elif [ $my_unpad -lt 1000 ]; then
  my_num="00${my_unpad}";
elif [ $my_unpad -lt 10000 ]; then
  my_num="0${my_unpad}";
else
  my_num="${my_unpad}";
fi;
echo "my_num: ${my_num}";
new_fname="${my_first}${my_num}${my_end}";
echo "  Command will be:" | tee -a rename.out;
echo "mv \"${orig}\" \"${new_fname}\"" | tee -a rename.out;
echo "    ..." | tee -a rename.out;
mv "${orig}" "${new_fname}" \
  && echo -e "        ... success\n" | tee -a rename.out \
  || echo -e "        ... FAILURE\n" | tee -a rename.out;
'



# or, if you don't want to see any display (and/or want it to complete faster),



# #Version that doesn't write to stdout, but runs more quickly
# (Above is the version that does show output and runs more slowly.)


find . -type f -iname "*.png" > fnames.lst; \
echo -e "\n\n  $(date +'%s_%Y-%m-%dT%H%M%S%z') \n" >> rename.out; \
find . -type f -iname "*.png" -print0 | \
xargs -I'{}' -0 bash -c '
orig="{}";
my_first=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*\)p\([0-9]\+\)[-][0-9]\+\([.]png\)$#\1#g'"'"');
my_end=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\3#g'"'"');
my_second=$(echo "${orig}" | \
  sed '"'"'s#^[.]/\(.*p\)\([0-9]\+\)[-][0-9]\+\([.]png\)$#\2#g'"'"');
my_num=0;
my_unpad=$(echo "${my_second}+1" | bc);
my_num=0;
if [ $my_unpad -lt 10 ]; then
  my_num="0000${my_unpad}";
elif [ $my_unpad -lt 100 ]; then
  my_num="000${my_unpad}";
elif [ $my_unpad -lt 1000 ]; then
  my_num="00${my_unpad}";
elif [ $my_unpad -lt 10000 ]; then
  my_num="0${my_unpad}";
else
  my_num="${my_unpad}";
fi;
new_fname="${my_first}${my_num}${my_end}";
echo "  Command will be:" >> rename.out;
echo "mv \"${orig}\" \"${new_fname}\"" >> rename.out;
echo "    ..." >> rename.out;
mv "${orig}" "${new_fname}" \
  && echo -e "        ... success\n" >> rename.out \
  || echo -e "        ... FAILURE\n" >> rename.out;
'


# (If you get nervous about progress and want to make sure things are actually happening, open another terminal, go to the same directory where you ran the previous command, and use the command, tail -f rename.out .)
"""
)

##endof:  if False
