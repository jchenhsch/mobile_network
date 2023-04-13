#!/bin/bash
#
# To install the pdftk:
#https://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/
#
# get rid of latex front page
pdftk Thesis_JiaxuanChen.pdf cat 2-r1 output Thesis_JiaxuanChen_1.pdf
# merge the thesis front page with thesis content
pdftk ThesisFrontPage.pdf Thesis_JiaxuanChen_1.pdf cat output Thesis_Jiaxuan_Chen.pdf
# remove the intermediate copy
rm Thesis_JiaxuanChen_1.pdf
 