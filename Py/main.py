from DfReadDataFile import *
from StSignificanceTesting import StSignificanceTesting, StSignificanceTestingCadVsRad
from UtilFigureOfMerit import UtilFigureOfMerit
from UtilFigureOfMerit import UtilLesionWeightsDistr
from UtilORVarComponents import testJackKnife



#ds = DfReadDataFile("extdata/toyFiles/FROC/frocCr.xlsx")
#ds = DfReadDataFile("extdata/Froc.xlsx")
ds = DfReadDataFile("extdata/JT.xlsx")
# val = UtilFigureOfMerit(ds, "wAfroc")
# ds = StSignificanceTesting("extdata/JT.xlsx")

# relWeights = [0.2, 0.3, 0.5]
# relWeights = 0
# lesWghtDistr = UtilLesionWeightsDistr(3, relWeights)
#FileName = "extdata/toyFiles/FROC/frocCr.xlsx"
# ds = DfReadDataFile("extdata/JT.xlsx")
# # pv = UtilPseudoValues(ds)
# # varCom = UtilORVarComponents(ds)
# #fomMeans = UtilORVarComponents(ds)
# st = StSignificanceTesting(ds)
# FileName = "extdata/JT.xlsx"
# ds = DfReadDataFile("extdata/NicoRadRoc.xlsx", DataType="ROC")
# dse = DfExtractDataset(ds, trts = [0,1], rdrs = [0,2])
#st = StSignificanceTesting(ds)
# ste = StSignificanceTesting(ds)
# st = StSignificanceTestingCadVsRad(ds, FOM = "Wilcoxon")
#fom = UtilFigureOfMerit(ds, FOM = "Wilcoxon")
jkFomValues = testJackKnife(ds, FOM = "wAfroc")
