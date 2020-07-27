from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#config.General.requestName = 'tutorial_TestApril2016_MC_analysis'
config.General.requestName = 'GENSIM_ExictedElec10k_M6000_16'
config.General.workArea = 'crab_projects_10k'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2.py'

#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-LHEGenElectron2000-3f22eb42fbc8c953391827da6f10333b/USER'
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-LHEGenElectron4000-3f22eb42fbc8c953391827da6f10333b/USER'
config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-LHEGenElectron6000-3f22eb42fbc8c953391827da6f10333b/USER'
###FOR Electron:
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-GI13TeVStep1_10K_Ele_M2000_04_02_18-3f22eb42fbc8c953391827da6f10333b/USER'
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-GI13TeVStep1_10K_Ele_M4000_04_02_18_2-3f22eb42fbc8c953391827da6f10333b/USER'
#config.Data.inputDataset ='/LHEGeneration_Ele/sdutt-GI13TeVStep1_10K_Ele_M6000_04_02_18-3f22eb42fbc8c953391827da6f10333b/USER'
config.Data.inputDBS = 'phys03'
config.Data.outputDatasetTag = 'GENSIM_ExictedElec10k_M6000_16'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Site.storageSite ='T2_IN_TIFR' 
