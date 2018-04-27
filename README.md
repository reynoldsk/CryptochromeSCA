# CryptochromeSCA
SCA for the Cryptochrome (CRY)/Photolyase family. The CRYs play a
critical role in the eukaryotic circadian clock. This analysis
accompanies: Rosensweig C, Reynolds KA, Gao P, Laothamatas I, Shan Y,
Ranganathan R, Takahashi JS, Green CB. (2018) "An evolutionary hotspot
defines functional differences between CRYPTOCHROMES" Nature
Communications v9:1138 


The analysis was performed using the pySCA toolbox (v.6.3) using a
series of shell scripts. This results in a pickle database (*.db)
containing the calculations. This database is loaded into a jupyter
notebook for further analysis and plotting. There are three options
for examining the data more closely:

1) To run the analysis completely from scratch, a user will first
need to install pySCA (https://github.com/reynoldsk/pySCA, for docs
see: http://reynoldsk.github.io/pySCA/) Once this is done, the jupyter
notebook describes how to repeat all of the calculations (and generate
the accompanying figures) from Rosensweig et al. 

2) If the user would like to interact with the pre-calculated data
(the SCA matrix, conservation values for each residue, etc) but
does not wish to install SCA, they can run the entire jupyter notebook
using the pre-calculated pickle db file in the Outputs directory
(Outputs/CYR20160414_20pct.db.gz). In this case, the database should
first be unzipped (using gunzip at the linux command line) and can
then be loaded into the jupyter notebook (SCA_Cry_Photolyase-vFin.ipynb)

3) If the user wishes to view the results (but not interact with
them/modify plots), we supply an html version of the notebook
(SCA_Cry_Photolyase-vFin.html)



