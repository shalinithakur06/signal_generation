import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

#process.GlobalTag.globaltag = '76X_mcRun2_asymptotic_v12'
#process.GlobalTag.globaltag = '74X_dataRun2_Prompt_v4'
#process.GlobalTag.globaltag =  '74X_dataRun2_Prompt_v2'
#process.GlobalTag.globaltag =  '76X_dataRun2_v15'
#process.GlobalTag.globaltag =  '74X_dataRun2_Prompt_v1'
#process.GlobalTag.globaltag  =  'MCRUN2_74_V9'
#process.GlobalTag.globaltag  =  '76X_dataRun2_v19'
#For Run2016 B-G (Data)
#process.GlobalTag.globaltag  =   '80X_dataRun2_2016LegacyRepro_v4'

#For 2016MC
process.GlobalTag.globaltag  =   '80X_mcRun2_asymptotic_2016_TrancheIV_v6'

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-20) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#'file:/afs/cern.ch/user/s/sdutt/work/WorkBook/CMSSW_8_0_25/src/demo/step4_Mu2000.root'
'file:AODSIM.root',
#'/store/mc/RunIISummer16DR80Premix/ZZ_TuneCUETP8M1_13TeV-pythia8/AODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/06676257-D7D7-E611-B8F0-00266CFCC804.root'
)
                            )

process.demo = cms.EDAnalyzer('underlying',
                              muon = cms.InputTag("muons"),
                              electrons = cms.InputTag("gedGsfElectrons"),
                              generalTrack = cms.InputTag("generalTracks"),
                              vertex = cms.InputTag("offlinePrimaryVertices"),
			      beamspot = cms.InputTag("offlineBeamSpot"),
                              bits = cms.InputTag("TriggerResults","","HLT"),
                              mcLabel = cms.InputTag("genParticles"),
                    	      pileupSummaryInfos = cms.InputTag("addPileupInfo"), 
			      genInfo = cms.InputTag("generator"),
                              isGen =cms.bool(True),
			      outputFile = cms.string("ZZ_27jan.root")
                              )

process.out = cms.OutputModule("PoolOutputModule",
				fileName = cms.untracked.string('ZZ_27jan.root')
			      )
process.TFileService = cms.Service("TFileService",fileName = cms.string('ZZ_27jan.root'))

process.p = cms.Path(process.demo)
