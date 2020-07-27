# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: generatorFrag_cfi.py --filein file:step1.root --fileout file:step2.root --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions auto:mc --beamspot Realistic8TeVCollision --step GEN,SIM --python_filename step2.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 64
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-64)
)

# Input source
process.source = cms.Source("PoolSource",
    secondaryFileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring('file:/afs/cern.ch/user/s/sdutt/work/WorkBook/CMSSW_8_0_25/src/signal_generation/step1.root')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('generatorFrag_cfi.py nevts:64'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('file:step2.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition

################################################################################
# Basic running parameters (modify to your needs)
index=1

#   random seed
theSeedValue = int(9583985+1000*index)
print 'Seed value: '+str(theSeedValue)

################################################################################



process.load('IOMC/RandomEngine/IOMC_cff')
process.RandomNumberGeneratorService.generator.initialSeed  = theSeedValue+111 ###cms.untracked.uint32(1136201) #########
process.RandomNumberGeneratorService.VtxSmeared.initialSeed = theSeedValue+222 ###cms.untracked.uint32(2132001)
process.RandomNumberGeneratorService.g4SimHits.initialSeed  = theSeedValue+333 ###cms.untracked.uint32(3136201)


process.generator = cms.EDFilter("Pythia8HadronizerFilter",
maxEventsToPrint = cms.untracked.int32(2),
pythiaPylistVerbosity = cms.untracked.int32(1),
filterEfficiency = cms.untracked.double(1.0),
pythiaHepMCVerbosity = cms.untracked.bool(True),
comEnergy = cms.double(13000.),
UseExternalGenerators = cms.untracked.bool(False),
PythiaParameters = cms.PSet(
processParameters = cms.vstring('Main:timesAllowErrors = 10000',
'Tune:pp 5'),
# 'Tune:ee 7' # most recent..,
# 'Tune:pp 14'),
parameterSets = cms.vstring('processParameters')
)
)

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.endjob_step,process.RAWSIMoutput_step)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions
# End of customisation functions
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 
