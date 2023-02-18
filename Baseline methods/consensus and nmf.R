
library(NMF) 
data=read.table("finaldata2.txt",header = F)
result=nmf(data,3)
group=predict(result)
group=t(group)
write.table(group,"nmflabel.txt",sep = ",")

d=as.matrix(data)
results = ConsensusClusterPlus(d,maxK=3,reps=50,pItem=0.8,pFeature=1,clusterAlg="hc",distance="pearson")
consensuslabel=results[[3]][["consensusClass"]]
write.table(consensuslabel,"consensuslabel.txt",sep=",")


