 
dat <- read.table('min_max_finaldata.txt',header = F)
dat = t(dat)
dat = dat[2:nrow(dat),2:ncol(dat)] 
dat = apply(dat,2,as.numeric)
for(p in 1:nrow(dat)){            
  matrix.p<-matrix(data = 0,nrow = ncol(dat), ncol = ncol(dat))       
  for(i in 1:ncol(dat)){  
    for(j in 1:ncol(dat)){ 
      matrix.p[i,j]= (dat[p,i]+dat[p,j])/2  
    }
  } 
  write.table(matrix.p,file=paste("mean_mRNA",p,".txt"), sep ="\t", quote =TRUE)
}

