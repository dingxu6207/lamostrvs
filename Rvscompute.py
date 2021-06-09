# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 13:06:06 2021

@author: dingxu
"""

import saphires as saph


tar,tar_spec = saph.io.read_ms('./salt1_rb.ls',combine_all=False,header_wave='Single')

temp = saph.io.read_pkl('./lte05500-4.50-0.0.PHOENIX-ACES-AGSS-COND-2011-HiRes_2800-11000_air.p',temp=True)

tar_spec = saph.utils.prepare(tar,tar_spec,temp)

tar_spec = saph.bf.compute(tar,tar_spec,vel_width=400,multiple_p = True)

tar_spec = saph.bf.analysis(tar,tar_spec,R=50000,single_plot=True,text_out = True,text_name = "file_name.txt")
