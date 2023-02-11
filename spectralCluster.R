library("SNFtool")

Data1=read.table("score_first.txt",sep="\t",header=F)
Data1=Data1[,1:178]
Data1=as.matrix(Data1)
label=spectralClustering(Data1,2)
label=t(label)
write.table(label,"label2.txt",sep =",", quote =TRUE) 
