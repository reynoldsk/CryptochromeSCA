#!/usr/bin/env python
"""
The scaMakeATS script performs a subset of the tasks in scaProcessMSA. The idea is to produce an alignment-to-structure (or alignment-to-reference sequence numbering) mapping for a specified sequence. In this version, the alignment is not trimmed at all before mapping. 
              
:Arguments: 
     Input_MSA.fasta (the alignment to be processed, typically the headers contain taxonomic information for the sequences).

:Keyword Arguments:
     --refpos, -o            reference positions, supplied as a text file with one position specified per line
     --refindex, -i          reference sequence number in the alignment, COUNTING FROM 0
     --output                specify a name for the outputfile

:Example: 
>>> ./scaMakeATS.py Inputs/CMGC_KinaseMSA.fasta -i 606 -o Refpos/CSNK2A2.pos --output CSNK2A2_ats.db

:By: Kim, Yusuf
:On: 11.21.2014
"""
from __future__ import division
import sys, time
import os
import numpy as np
import copy
import scipy.cluster.hierarchy as sch
import scaTools as sca
import pickle
import argparse
from Bio import SeqIO
from scipy.io import savemat

if __name__ =='__main__':
	#parse inputs
        parser = argparse.ArgumentParser()


        parser = argparse.ArgumentParser()
        parser.add_argument("alignment", help='Input Sequence Alignment')
        parser.add_argument("-o","--refpos", dest = "refpos", help="reference positions, supplied as a text file with one position specified per line")
        parser.add_argument("-i","--refindex", dest = "i_ref", type = int, help="reference sequence number in the alignment, COUNTING FROM 0")
        parser.add_argument("--output", dest="outputfile", default = None, help="specify an outputfile name")
        options = parser.parse_args()

	# Read in initial alignment
        headers_full, sequences_full = sca.readAlg(options.alignment)
        print('Loaded alignment of %i sequences, %i positions.' % (len(headers_full), len(sequences_full[0])))

	# Create the ATS
        i_ref = options.i_ref
        print "Reference sequence %i:" % (i_ref)
        print headers_full[i_ref]
        s_tmp = sequences_full[i_ref]

        try:
                f = open(options.refpos,'r')
                ats_tmp = [line.rstrip('\n') for line in f]
                print ats_tmp
                f.close()
        except:
                sys.exit("Error!! Unable to read reference positions!")
        try:
                sequences, ats = sca.makeATS(sequences_full, ats_tmp, s_tmp, i_ref)
        except:
                sys.exit("Error!! Unable to make ATS!")

	print "Final alignment parameters:"
	print "Number of positions: L = %i" % (len(s_tmp))
        print "Size of ats: %i" % len(ats)

	# saving the important stuff. Everything is stored in a file called [MSAname]_sequence.db. 
	path_list = options.alignment.split(os.sep)
	fn = path_list[-1]
	fn_noext = fn.split(".")[0]

	D = {}
	D['alg'] = sequences_full
	D['hd'] = headers_full
	D['ats'] = ats
        D['i_ref'] = i_ref
        
        if (options.outputfile is not None):
                fn_noext = options.outputfile
	db = {}
	db['sequence']=D
	pickle.dump(db,open(fn_noext + ".db","wb"))
		
