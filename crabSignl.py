from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#config.General.requestName = 'tutorial_TestApril2016_MC_analysis'
config.General.requestName = 'Ele6000'
config.General.workArea = 'crab_projects_10k'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../demo/underlying/test/mc_ConfFile_cfg.py'


#config.Data.inputDataset = '/GenericTTbar/atanasi-CRAB3_tutorial_April2016_MC_analysis-37773c17ce2994cf16892d5f04945e41/USER'
#config.Data.inputDBS = 'global'
#config.Data.outputDatasetTag = 'CRAB3_tutorial_TestApril2016_MC_analysis'

###FOR Ele Mass
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-RecoToAOD_Ele2000_16-621ef74ae1dffa0013deb3f67a853a30/USER'
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-RecoToAOD_Ele4000_16-621ef74ae1dffa0013deb3f67a853a30/USER'
config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-RecoToAOD_Ele6000_16-621ef74ae1dffa0013deb3f67a853a30/USER'

config.Data.inputDBS = 'phys03'
config.Data.outputDatasetTag = 'underlying'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 36
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Site.storageSite ='T2_IN_TIFR' 
