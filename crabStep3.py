from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#config.General.requestName = 'tutorial_TestApril2016_MC_analysis'
config.General.requestName = 'LHEGen_DIGIHLTEle6000_16'
config.General.workArea = 'crab_projects_10k'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3.py'


###FOR Ele Mass
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-GENSIM_ExictedElec10k_M2000_16-1da7e8d10d3dce19fe8c9962cab747ac/USER'
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-GENSIM_ExictedElec10k_M4000_16-1da7e8d10d3dce19fe8c9962cab747ac/USER'
config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-GENSIM_ExictedElec10k_M6000_16-1da7e8d10d3dce19fe8c9962cab747ac/USER'


##first round
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-GENSIM_ExictedElec10k_M2000_100Evts-1da7e8d10d3dce19fe8c9962cab747ac/USER'
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-GENSIM_ExictedElec10k_M4000_100Evts-1da7e8d10d3dce19fe8c9962cab747ac/USER'
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-GENSIM_ExictedElec10k_M6000_100Evts-1da7e8d10d3dce19fe8c9962cab747ac/USER'
config.Data.inputDBS = 'phys03'
config.Data.outputDatasetTag = 'LHEGenDIGIHLTEleM6000_16'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#config.Data.splitting = 'EventAwareLumiBased'
#config.Data.unitsPerJob = 2
#NJOBS = 6  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Site.storageSite ='T2_IN_TIFR' 
