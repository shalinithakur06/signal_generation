
from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()
config.General.requestName = 'GIStep1_Ele_6000_4'
config.General.workArea = 'crab_projects_10k'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'PrivateMC'
#config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step1.py'
#config.JobType.inputFiles= ['GIset1.lhe','GIset_4000.lhe','GIset_5000.lhe','GIset_8000.lhe','GIset_9200.lhe','GIset_9500.lhe','GIset_9800.lhe']
config.JobType.inputFiles= ['GIEle_6000.lhe']
config.Data.outputPrimaryDataset = 'LHEGeneration_Ele'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 16
NJOBS = 625  # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
#config.Data.outLFNDirBase = '/dpm/indiacms.res.in/home/cms/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputDatasetTag = 'LHEGenElectron6000'

config.Site.storageSite = 'T2_IN_TIFR'
