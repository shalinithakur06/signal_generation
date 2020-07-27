from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

#config.General.requestName = 'tutorial_TestApril2016_MC_analysis'
config.General.requestName = 'RecoToAOD_Ele6000_16'
config.General.workArea = 'crab_projects_10k'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step4.py'


#config.Data.inputDataset = '/GenericTTbar/atanasi-CRAB3_tutorial_April2016_MC_analysis-37773c17ce2994cf16892d5f04945e41/USER'
#config.Data.inputDBS = 'global'
#config.Data.outputDatasetTag = 'CRAB3_tutorial_TestApril2016_MC_analysis'

#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-LHEGenDIGIHLTEleM2000_16-47b3fc5c014a84fcbbb4d5b57004382c/USER'
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-LHEGenDIGIHLTEleM4000_16-47b3fc5c014a84fcbbb4d5b57004382c/USER'
config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-LHEGenDIGIHLTEleM6000_16-47b3fc5c014a84fcbbb4d5b57004382c/USER'
###FOR Ele Mass
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-LHEGen_DIGIHLTEleM2000-47b3fc5c014a84fcbbb4d5b57004382c/USER'
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-LHEGen_DIGIHLTEleM4000-47b3fc5c014a84fcbbb4d5b57004382c/USER'
#config.Data.inputDataset = '/LHEGeneration_Ele/sdutt-LHEGen_DIGIHLTEleM6000-47b3fc5c014a84fcbbb4d5b57004382c/USER'
config.Data.inputDBS = 'phys03'
config.Data.outputDatasetTag = 'RecoToAOD_Ele6000_16'

config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True

config.Site.storageSite ='T2_IN_TIFR' 
