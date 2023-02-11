# GCNA-cluster: A Gene Co-expression Network Alignment to Cluster Cancer Patients Algorithm for Identifying Subtypes of Pancreatic Ductal Adenocarcinoma
First, the GCNA-cluster algorithm constructed a weighted gene co-expression network for each patient.Secondly, network alignment was performed between pairs of gene co-expression networks, and the score of alignment was the similarity between patients. By extrapolating from this, a patient-patient similarity matrix can be obtained. Finally, cluster patients according to their similarity.
## The environment of GCNA-cluster
Rstudio 4.0.2<br>
Matlab R2016a
## Code and data
### Raw data
For the cancer data used in the paper, the TCGA database (https://portal.gdc.cancer.gov/) and the GEO database (https://www.ncbi.nlm.nih.gov/geo/, GEO accession: GSE15471 and GSE17891) were used. 
### 生成基因共表达网络
Use the `gene expression.txt` file in the `TCGA_Network` or `GEO_Network` folder as input and run `onePatienNet.R` to generate the patient's gene co-expression network.
### 网络比对
……
### 聚类
……
