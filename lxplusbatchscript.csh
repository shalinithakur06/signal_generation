#!/bin/tcsh
source /cvmfs/cms.cern.ch/cmsset_default.csh
set CMSSW_PROJECT_SRC="/afs/cern.ch/user/s/sdutt/work/WorkBook/CMSSW_8_0_25/src"
set CFG_FILE="step3.py"
set OUTPUT_FILE="RAWSIM.root"
set TOP="$PWD"

cd $CMSSW_PROJECT_SRC
eval `scramv1 runtime -csh`
cd $TOP
cmsRun /afs/cern.ch/user/s/sdutt/work/WorkBook/CMSSW_8_0_25/src/signal_generation/$CFG_FILE
rfcp RAWSIM.root /afs/cern.ch/user/s/sdutt/work/WorkBook/CMSSW_8_0_25/src/signal_generation/$OUTPUT_FILE
